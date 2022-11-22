from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file("test.kv")

class MyLayout(FloatLayout):
    pass
        
class MyApp(App):
    def build(self):
        return MyLayout()

# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()