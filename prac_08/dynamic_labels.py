"""
time est
est: 20 min
actual: 28 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Name 1', 'Name 2', 'Name 3']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create Labels from the list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        """Clear all the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
