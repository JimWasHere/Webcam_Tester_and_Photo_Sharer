from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from kivy.core.clipboard import Clipboard
import webbrowser
from filesharer import FileSharer


kv = Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    # start the webcam and changes Button text
    def start(self):
        """starts camera and changes button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    # stop the webcam
    def stop(self):
        """stops camera and changes button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    # capture a photo
    def capture(self):
        """creates filename with current time and takes photo
        and saves it under filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"picture_files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        """Accesses photo filepath, uploads it to the web and inserts
        the link into the widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """attempts to copy link to photo, if none found, creates one and
        copies it"""
        try:
            Clipboard.copy(self.url)
        except AttributeError:
            self.create_link()
            Clipboard.copy(self.url)

    def open_link(self):
        """attempts to open link to photo, if none found, creates one and
        opens it"""
        try:
            webbrowser.open(self.url)
        except AttributeError:
            self.create_link()
            webbrowser.open(self.url)


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()





