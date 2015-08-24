from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class Principal(Screen):
    def mostrar(self):
        print("Principal")

class Bienvenido(Screen):
    def mostrar(self):
        #self.nombre= nombre
        print("Bienvenido")

class SaludoApp(App):

    def build(self):
        root = ScreenManager()
        root.add_widget(Principal(name='principal'))
        root.add_widget(Bienvenido(name='bienvenido'))
        return root


if __name__ == '__main__':
    SaludoApp().run()
