import kivy
import qrcode
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Root(Widget):
    url = ObjectProperty(None)
    convert = ObjectProperty(None)

    def generate(self):
        # user url input
        data = self.url.text

        img = qrcode.make(data)

        img.show()

        self.url.text = ""


class QRGenerator(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    QRGenerator().run()
