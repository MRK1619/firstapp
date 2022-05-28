import kivy
from kivy.app import App
from kivy.uix.label import Label


class ParthaApp(App):
    
    def build(self):
        return Label(text="Partha Sarathi Hazra")


if __name__=="__main__":
    ParthaApp().run()