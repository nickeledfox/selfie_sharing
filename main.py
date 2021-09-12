from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from cam_screen import CameraScreen
from img_screen import ImageScreen

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()