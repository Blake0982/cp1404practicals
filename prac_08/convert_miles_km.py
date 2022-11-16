from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

MILES_KILOMETRES_RATIO = 1.60934


class MileToKmApp(App):
    """ """

    def build(self):
        Window.size = (800, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            kilometres = float(value) * MILES_KILOMETRES_RATIO
            self.root.ids.output_label.text = str(f"{kilometres:.3f}")
        except ValueError:
            kilometres = 0
            self.root.ids.output_label.text = str(kilometres)

    def handle_increment(self, value, increment):
        try:
            miles = float(value) + increment
            self.root.ids.input_number.text = str(miles)
        except ValueError:
            miles = 0 + increment
            self.root.ids.input_number.text = str(miles)


MileToKmApp().run()
