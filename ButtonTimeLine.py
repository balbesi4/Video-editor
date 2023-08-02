from tkinter import *
from ButtonFragment import ButtonFragment


class ButtonTimeLine:
    def __init__(self, gui, time_line):
        self.time_line = time_line
        self.gui = gui
        canvas = Canvas(self.gui.window, bg="blue")
        canvas.pack(anchor="ne", fill=BOTH, expand=True)

        self.frame = Frame(canvas,  bg="blue")
        # self.frame.pack_propagate(False)
        # self.frame.configure(width=750, height=300)
        self.frame.pack(anchor="ne", fill='both', expand=True)
        canvas.create_window(0, 0, window=self.frame, anchor="ne")

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
            ButtonFragment(self.gui, self, fragment)