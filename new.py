import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from matplotlib.pyplot import text
from kivy.uix.button import Button


class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name:"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        
        self.add_widget(Label(text="Student Marks:"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)
        
        self.add_widget(Label(text="Student Rollnumber:"))
        self.s_rolls = TextInput()
        self.add_widget(self.s_rolls)

        self.press = Button(text="Click Me ")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press) 

    def click_me(self,instance):
            print("Name of the student is: " + self.s_name.text)  
            print("Marks of student is: " + self.s_marks.text)
            print("Roll number of studet is: " + self.s_rolls.text)
class ParthaApp(App):
    def build(self):
        return Layout()
    
if __name__=="__main__":
    ParthaApp().run()


    