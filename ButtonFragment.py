from Fragment import Fragment
from tkinter import *


class ButtonFragment:
    def __init__(self, gui, button_time_line, fragment: Fragment):
        self.gui = gui
        self.picked = False
        self.button_time_line = button_time_line
        self.fragment = fragment
        self.default_font = ("Roboto", 12, "bold")
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.button = Button(
            self.button_time_line.frame,
            text=f"{fragment.name}",
            bg="#72FEFE",
            font=self.default_font,
            # image=self.pixelVirtual,
            anchor="center",
            compound="center",
            height=10,
            width=10,
            command=self.on_click
        )
        self.button.pack(side='left')

    def on_click(self):
        self.gui.picked_indexes.append(self.fragment.id)