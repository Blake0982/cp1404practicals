from kivy.app import App
from kivy.lang import Builder


class MileToKmApp(App):
    """ """

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            result = 0
            self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, increment):
        try:
            result = float(value) + increment
            self.root.ids.input_number.text = str(result)
        except ValueError:
            result = 0 + increment
            self.root.ids.input_number.text = str(result)


MileToKmApp().run()
