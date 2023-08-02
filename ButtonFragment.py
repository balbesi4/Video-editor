from Fragment import Fragment
from tkinter import *


class ButtonFragment:
    def __init__(self, gui, button_time_line, fragment: Fragment):
        self.gui = gui
        self.picked = False
        self.button_time_line = button_time_line
        self.fragment = fragment
        self.default_font = ("Roboto", 12, "bold")
        self.pixel_virtual = PhotoImage(width=1, height=1)
        self.button = Button(
            self.button_time_line.frame,
            text=f"{fragment.name}",
            bg="#72FEFE",
            font=self.default_font,
            anchor="center",
            image=self.pixel_virtual,
            width=220,
            height=220,
            compound="center",
            command=self.on_click
        )
        self.button.pack(side=LEFT, padx=20, pady=20)

    def on_click(self):
        if self.picked:
            self.button.configure(bg="#72FEFE")
            self.gui.picked_indexes.remove(self.fragment.id)
            self.picked = False
        else:
            self.button.configure(bg="green")
            self.gui.picked_indexes.append(self.fragment.id)
            self.picked = True
