"""Real time plotting of Microphone level using kivy
"""


import audioop
import pyaudio
from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread
from kivy.uix.widget import Widget
from ScreenResolution import ScreenResolution


Builder.load_string("""
<AudioVisualizerGraph>:
    
    BoxLayout:
        size: 222,222 
        pos: 0 ,0
        orientation: "vertical"
        Graph:
            id: graph
            
""")


def get_microphone_level():
    import Dialog
    """
    source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    audioop.max alternative to audioop.rms
    """
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()

    s = p.open(format=FORMAT,
               channels=CHANNELS,
               rate=RATE,
               input=True,
               frames_per_buffer=chunk)

    while True:
        data = s.read(chunk)
        mx = audioop.rms(data, 2)/20
        if len(Dialog.levels) >= 100:
            Dialog.levels.pop(0)
        Dialog.levels.append(mx)


class AudioVisualizerGraph(Widget):

    def __init__(self,):
        get_level_thread = Thread(target = get_microphone_level)
        get_level_thread.daemon = True
        get_level_thread.start()
        super(AudioVisualizerGraph, self).__init__()
        self.plot = MeshLinePlot(color=[1, 1, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.01)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        import Dialog
        self.plot.points = [(i, j/5) for i, j in enumerate(Dialog.levels)]


class RealTimeMicrophone(App):
    screenResolution = ScreenResolution()
    def build(self):
        return AudioVisualizerGraph()

if __name__ == "__main__":
    levels = []
   
    RealTimeMicrophone().run()
    
