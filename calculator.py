import os
import platform

from kivy.core.text import LabelBase
from assets.colors import colors

from kivy.core.window import Window
from kivymd.app import MDApp
from libs.uix.baseclass.home_screen import HomeScreen
from libs.uix.baseclass.mymdflatbutton import MyMDFlatButton

from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

LabelBase.register(name='Lato', fn_regular='assets/fonts/Lato-Regular.ttf',
                   fn_bold='assets/fonts/Lato-Bold.ttf')


class Calculator(MDApp):  # NOQA: N801

    def update_label(self):
        # HomeScreen().lbl.text = self.formula
        sf.ids.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(MyMDFlatButton().text)
        self.update_label()

    def add_operator(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = '0'

    def cancel_calc(self, instance):
        self.formula = '0'
        self.update_label()

    def delete_num(self, instance):
        self.formula = self.formula[0:-1]
        self.update_label()

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

        Window.soft_input_mode = "below_target"
        Window.size = (360, 640)
        sf = HomeScreen()
        self.title = "Calculator"

        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build(self):
        self.formula = '0'
        return Root()
