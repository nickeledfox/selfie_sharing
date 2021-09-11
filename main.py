from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from picture_sharer import FileSharer
import time

Builder.load_file('uix.kv')

class CameraScreen(Screen):
    def start(self):
        # Run camera
        self.ids.camera.play = True
        self.ids.camera_btn.text = 'Stop'
        self.ids.camera.texture = \
            self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_btn.text = 'Play'
        self.ids.camera.texture = None

    def capture(self):
        # Generates picture name based on current date/time
        capture_time = time.strftime('%H.%M.%S-%Y:%m:%d')

        # Sends the picture to the "pictures" folder
        pictures_path = f'pictures/{capture_time}.png'
        self.ids.camera.export_to_png(pictures_path)

        # Displays the picture after it's capture on the image screen
        self.manager.current = 'image_screen'
        self.manager.current_screen\
            .ids.picture.source = pictures_path


class ImageScreen(Screen):
    def create_link(self):
        # Generates filestack link
        picture_path = self.ids.picture.source
        file_sharer = FileSharer(filepath=picture_path)
        url = file_sharer.share()
        self.ids.link.text = url


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()