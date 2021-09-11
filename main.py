from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from sharing import Sharing
import time

Builder.load_file('uix.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_btn.text = 'Stop'
        self.ids.camera.texture = \
            self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_btn.text = 'Play'
        self.ids.camera.texture = None

    def capture(self):
        capture_time = time.strftime('%H.%M.%S-%Y:%m:%d')
        file_name = capture_time + '.png'
        self.ids.camera.export_to_png(file_name)


class ImageScreen:
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()