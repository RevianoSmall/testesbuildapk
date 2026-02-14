from kivy.app import App
from kivy.uix.button import Button

class AplikasiBos(App):
    def build(self):
        return Button(text="Halo Bos!\nAPK Tanpa Lag!", font_size=50, halign="center")

if __name__ == "__main__":
    AplikasiBos().run()
