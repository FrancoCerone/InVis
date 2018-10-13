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
        pos: -5,-5
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
        mx = audioop.rms(data, 2)/10
        if len(Dialog.levels) >= 100:
            Dialog.levels = Dialog.levels[:-1]
        Dialog.levels.insert(0,mx)


class AudioVisualizerGraph(Widget):
    def __init__(self,):
        get_level_thread = Thread(target = get_microphone_level)
        get_level_thread.daemon = True
        get_level_thread.start()
        super(AudioVisualizerGraph, self).__init__()
        mesh_plot = LinePlot()
        self.plot = mesh_plot
        self.ids.box.size = screenResolution.get_width()+10,screenResolution.get_height()+10

    def start(self):
        self.stop()
        self.plot = LinePlot(color=[1,1,0,1], line_width= 8)
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
    def get_plot(self):
        self.plot
    
    
        



    
