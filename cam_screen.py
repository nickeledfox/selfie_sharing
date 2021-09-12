import time
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('cam_screen.kv')

class CameraScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Generates picture name based on current date/time
        self.capture_time =\
            time.strftime('%H.%M.%S-%Y:%m:%d')

        self.pictures_path =\
            f'pictures/{self.capture_time}.png'

    def start(self):
        # Run camera
        self.ids.camera.play = True
        self.ids.camera_btn.text = 'Stop'
        self.ids.camera.texture =\
            self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_btn.text = 'Play'
        self.ids.camera.texture = None

    def capture(self):
        # Sends the picture to the "pictures" folder
        self.ids.camera.export_to_png(self.pictures_path)

        # Displays the picture after it's capture on the image screen
        self.manager.current = 'image_screen'
        self.manager.current_screen\
            .ids.picture.source = self.pictures_path