import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, Gdk, Gio

# bytes = Gio.resources_lookup_data("style/style", 0)
css_provider = Gtk.CssProvider()
with open('src/style/style.css', 'r') as f:
    css_provider.load_from_data(f.read().encode())
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

languages = [
    'Olá, mundo!',
    'Hello, world!',
    'Bonjour, le monde',
    'こんにちは世界',
    'Привет, мир',
    'Hola, Mundo',
    '안녕하세요, 세상'
]

class Window(Gtk.Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.set_default_size(500, 500)
        self.set_resizable(False)

        self.connect('destroy', self.on_destroy)

        # main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box = Gtk.CenterBox(orientation=Gtk.Orientation.VERTICAL)
        scale_box = Gtk.CenterBox(orientation=Gtk.Orientation.VERTICAL)
        self.label = Gtk.Label(label=languages[0])
        self.scale = Gtk.Scale()
        self.header = Gtk.HeaderBar()

        self.scale.connect('value-changed', self.on_scale_changed)

        self.scale.set_digits(0)
        self.scale.set_range(0, len(languages) - 1)

        self.set_child(main_box)

        main_box.set_end_widget(scale_box)
        #main_box.append(label_box)

        self.header.set_css_classes(['header'])
        self.label.set_css_classes(['label'])
        self.scale.set_css_classes(['scale'])

        self.set_titlebar(self.header)

        main_box.set_center_widget(self.label)
        scale_box.set_start_widget(self.scale)

    def on_scale_changed(self, scale):
        scale.set_value(round(scale.get_value()))
        self.label.set_label(languages[int(scale.get_value())])

    def on_destroy(self, window):
        Gtk.main_quit()

