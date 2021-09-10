from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from sharing import Sharing

Builder.load_file('uix.kv')

class CameraScreen(Screen):
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen:
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()