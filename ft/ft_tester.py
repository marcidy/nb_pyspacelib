from ft import (
    ftclient,
    ftdevice
)
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse
from functools import partial
from ft_controller import (
    FTController,
    FTImage,
)
import pudb


class FlaschenTaschen(App):

    ftc = FTController()
    ft = ftdevice("ft", "ft.noise", 1337, 45, 35)

    def add_bottles(self, label, wid, width, height, *largs):
        self.fti = FTImage("./test.png", "./")
        self.fti.pixelate(self.ft.width, self.ft.height)
        self.ftc.fill_buffer(self.fti)
        grid = self.ftc.grid
        min_val = 5  # used to work-around layering

        with wid.canvas:
            for y in range(width):
                for x in range(height):
                    r, g, b = grid[height-(x+1)][y]
                    Color(max(r, min_val)/255,
                          max(g, min_val)/255,
                          max(b, min_val)/255)
                    Ellipse(pos=(y*20, x*20), size=(20, 20))

    def reset(self, label, wid, *largs):
        label.text = "Reset"
        wid.canvas.clear()

    def show(self, label, wid, *largs):
        self.ftc.show()

    def build(self):
        wid = Widget()
        label = Label(text="0")

        btn_add100 = Button(
            text='build FT', on_press=partial(
                self.add_bottles, label, wid, self.ft.width, self.ft.height))

        btn_reset = Button(text="Reset",
                           on_press=partial(self.reset, label, wid))

        btn_push = Button(
            text="Show on FT",
            on_press=partial(
                self.show,
                label,
                wid)
        )

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(btn_reset)
        layout.add_widget(btn_push)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == "__main__":
    FlaschenTaschen().run()
