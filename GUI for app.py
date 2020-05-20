from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup
from Storage import AccountStorage
"         Screen Dimensions         "
"         Standard Phone Size         "
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

class LogoScreen(Screen):
    pass

class CreateAccountScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def entry(self):
        if self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                storage.add_user(self.email.text, self.password.text)

                self.reset()

            else:
                invalidForm()
        else:
            invalidLogin()

    def login(self):
        self.reset()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginButton(self):
        if storage.validate(self.email.text, self.password.text):
            self.reset()

    def createButton(self):
        self.reset()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class HomeScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

GUI = Builder.load_file("main.kv")

storage = AccountStorage("accountstorage.txt")

class MainApp(App):
    title = "Zutto App"

    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


if __name__ == "__main__":
    MainApp().run()
