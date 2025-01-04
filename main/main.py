from kivy.app import App
from kivy.uix.label import Label
from plyer import gps
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from android.permissions import request_permissons, Permission

class GpsApp(App):
    def build(self):
        self.label = Label(text = '获取位置中...')
        gps.configure()

    pass
class waterApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')

        self.label = Label(text = '多喝热水', font_size = '20sp')
        layout.add_widget(self.label)

        buttonHigh = Button(text = '稍热', font_size = '20sp')
        buttonModerate = Button(text = '适中', font_size = '20sp')
        buttonLow = Button(text = '稍冷', font_size = '20sp')

        layout.add_widget(buttonHigh)
        layout.add_widget(buttonModerate)
        layout.add_widget(buttonLow)

        return super().build()
    def high_press():
        pass
    def moderate_press():
        pass
    def low_press():
        pass
    