from tkinter import *
from ButtonFragment import ButtonFragment


class ButtonTimeLine:
    def __init__(self, gui, time_line):
        self.time_line = time_line
        self.gui = gui
        self.buttons = []
        canvas = Canvas(self.gui.window, width=750, height=300)
        canvas.place(x=300)

        # создаем фрейм на канвасе
        self.frame = Frame(canvas, bd=2)
        self.frame.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # настраиваем скроллбар
        scrollbar = Scrollbar(self.gui.window, orient='horizontal',
                              command=canvas.xview)
        scrollbar.place(relx=0.29, rely=0.54, relwidth=0.71, anchor='sw')
        canvas.configure(xscrollcommand=scrollbar.set)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        self.frame.bind('<Configure>', on_frame_configure)

    def update(self):
        for child in self.frame.winfo_children():
            child.destroy()

        for fragment in self.time_line.time_line:
            self.buttons.append(ButtonFragment(self.gui, self, fragment))