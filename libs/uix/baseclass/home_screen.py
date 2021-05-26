from kivymd.uix.screen import MDScreen


import utils

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):
    """
    Example Screen.
    """

    # def update_label(self):
    #     HomeScreen().ids.lbl.text = self.formula

    # def add_number(self, instance):
    #     if self.formula == '0':
    #         self.formula = ''
    #     self.formula += str(instance.text)
    #     self.update_label()
