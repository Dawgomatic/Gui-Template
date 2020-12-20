import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


# object for the mainscreen.
class MainWindow(Screen):
    pass


# object to manage general aspects of all screens.
class WindowManager(ScreenManager):
    # set background color of all screens to white. Colors are in rgba format.
    Window.clearcolor = (1, 1, 1, 1)
    pass


# tells where return will pull infomation from this is a library specific feature.
kv = Builder.load_file("ui.kv")


# forms an object for the containment of all other code.
class Template(App):
    def build(self):
        return kv


# starts application.
Template().run()
