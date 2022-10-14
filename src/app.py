from sys import argv
import gi

gi.require_version('Adw', '1')

from gi.repository import Adw
from window import Window

class App(Adw.Application):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = Window(application=app)
        self.win.present()

app = App(application_id='local.hello-gtk')
app.run(argv)
