from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from picture_sharer import FileSharer

Builder.load_file('img_screen.kv')

class ImageScreen(Screen):
    def create_link(self):
        # Generates filestack link
        picture_path = App.get_running_app()\
            .root.ids.camera_screen.pictures_path
        file_sharer = FileSharer(filepath=picture_path)
        self.url = file_sharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = 'Create a Link First'
