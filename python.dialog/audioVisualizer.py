"""Real time plotting of Microphone level using kivy
"""


import audioop
import pyaudio
from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.garden.graph import Graph, SmoothLinePlot, MeshStemPlot,ContourPlot, LinePlot
from kivy.clock import Clock
from threading import Thread
from kivy.uix.widget import Widget
from ScreenResolution import ScreenResolution
from kivy.utils import get_color_from_hex as rgb
#from cycler import cycler
#import numpy as np
#import matplotlib.pyplot as plt
screenResolution = ScreenResolution()

Builder.load_string("""
<AudioVisualizerGraph>:
    BoxLayout:
        size: 100,100
        pos: 0 ,0
        id: box
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
        mx = audioop.rms(data, 2)/60
        if len(Dialog.levels) >= 100:
            Dialog.levels = Dialog.levels[:-1]
        Dialog.levels.insert(0,mx)


class AudioVisualizerGraph(Widget):
    def __init__(self,):
        get_level_thread = Thread(target = get_microphone_level)
        get_level_thread.daemon = True
        get_level_thread.start()
        super(AudioVisualizerGraph, self).__init__()
        
        
        graph_theme = {
            'label_options': {
                'color': rgb('444444'),  # color of tick labels and titles
                'bold': True},
            'background_color': rgb('f8f8f2'),  # back ground color of canvas
            'tick_color': rgb('808080'),  # ticks and grid
            'border_color': rgb('808080')}  # border drawn around each graph

        graph = Graph(
                    xlabel='Cheese',
                    ylabel='Apples',
                    x_ticks_minor=5,
                    x_ticks_major=25,
                    y_ticks_major=1,
                    y_grid_label=True,
                    x_grid_label=True,
                    padding=5,
                    xlog=False,
                    ylog=False,
                    x_grid=True,
                    y_grid=True,
                    xmin=-50,
                    xmax=50,
                    ymin=-1,
                    ymax=1,
                    **graph_theme)
        
        mesh_plot = LinePlot(color=[1,0,0,1], line_width= 8)
        #mesh_plot = MeshStemPlot(color=[1,1,1,1])
        #mesh_plot =ContourPlot(color=[1,1,1,1])
        self.plot = mesh_plot
        self.ids.box.size = screenResolution.get_width(),screenResolution.get_height()

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.01)

    def stop(self):
        import Dialog
        Clock.unschedule(self.get_value)
        Dialog.levels = []
        self.ids.graph.remove_plot(self.plot)
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
    
