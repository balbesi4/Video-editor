from Fragment import Fragment
from tkinter import *
import moviepy.editor as mp


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
            height=200,
            compound="center",
            command=self.on_click
        )
        self.button.grid(row=1, column=self.button_time_line.last_column, padx=20, pady=20)

        self.info_button = Button(
            self.button_time_line.frame,
            text="Информация",
            font=("Roboto", 10),
            anchor="center",
            image=self.pixel_virtual,
            width=220,
            height=10,
            compound="center",
            command=lambda: self.on_info_click()
        )
        self.info_button.grid(row=0, column=self.button_time_line.last_column, padx=20, pady=10)
        self.button_time_line.last_column += 1

    def on_click(self):
        if self.picked:
            self.button.configure(bg="#72FEFE")
            self.gui.picked_indexes.remove(self.fragment.id)
        else:
            self.button.configure(bg="green")
            self.gui.picked_indexes.append(self.fragment.id)
        self.picked = not self.picked
        self.gui.toggle_buttons()

    def on_info_click(self):
        top_level = Toplevel()
        top_level.grab_set()
        top_level.resizable(False, False)
        top_level.geometry("300x80")
        label_1 = Label(top_level, text=f"Информация о фрагменте {self.fragment.id + 1}")
        label_1.pack(side=TOP)
        label_2 = Label(top_level, text=f"Длительность клипа: {self.fragment.clip.duration}")
        label_2.pack(side=TOP)
        label_3_text = "Аудио не установлено" if self.fragment.clip.audio is None else f"Громкость клипа: {str(self.fragment.clip.audio.set_fps(44100).max_volume())[0:4]}"
        label_3 = Label(top_level, text=label_3_text)
        label_3.pack(side=TOP)
