import moviepy.editor as mp
from tkinter import messagebox, filedialog

from ButtonTimeLine import ButtonTimeLine
from Fragment import Fragment
from TimeLine import TimeLine
from tkinter import *


class GraphicalUserInterface:
    def __init__(self):
        self.time_line = TimeLine()
        self.picked_indexes = []
        self.window = Tk()
        self.window.title("Svindeo")
        self.window.geometry("1050x550")
        self.window.resizable(False, False)
        self.main_font = ("Roboto", 12, "bold")

        self.main_frame = Frame(self.window, bg="#C5D0C5")
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=300, height=300)
        self.main_frame.pack(anchor="nw")
        self.main_frame.grid_columnconfigure(0, minsize=300)

        self.upload_video_button = Button(
            self.main_frame,
            height=2,
            font=self.main_font,
            text="Загрузить видео",
            bg="#938CDD",
            command=lambda: self.upload_video_handler()
        )
        self.upload_image_button = Button(
            self.main_frame,
            height=2,
            font=self.main_font,
            text="Загрузить картинку",
            bg="#938CDD"
        )
        self.export_button = Button(
            self.main_frame,
            height=2,
            font=self.main_font,
            text="Сохранить",
            bg="#938CDD",
            command=lambda: self.export_handler()
        )
        self.undo_button = Button(
            self.main_frame,
            height=2,
            font=self.main_font,
            text="Отмена",
            bg="#938CDD",
            fg="#AFFFFF",
            command=lambda: self.undo_command_handler()
        )
        self.upload_video_button.grid(row=0, column=0, stick="we", padx=25, pady=12)
        self.upload_image_button.grid(row=1, column=0, stick="we", padx=25, pady=12)
        self.export_button.grid(row=2, column=0, stick="we", padx=25, pady=12)
        self.undo_button.grid(row=3, column=0, stick="we", padx=25, pady=12)

        self.command_frame = Frame(self.window, bg="#A055D3")
        self.command_frame.propagate(False)
        self.command_frame.configure(width=800, height=250)
        self.command_frame.pack(side=BOTTOM)
        self.command_frame.grid_columnconfigure(0, minsize=275)
        self.command_frame.grid_columnconfigure(1, minsize=250)
        self.command_frame.grid_columnconfigure(2, minsize=275)
        self.command_frame.grid_columnconfigure(3, minsize=250)

        self.change_speed_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Изменить скорость"
        )
        self.change_volume_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Изменить громкость"
        )
        self.concatenate_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Склеить фрагменты"
        )
        self.crop_clip_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Обрезать фрагмент"
        )
        self.crop_picture_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Кроп картинки"
        )
        self.fade_in_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Fade in"
        )
        self.fade_out_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Fade out"
        )
        self.remove_audio_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Убрать аудио"
        )
        self.reverse_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Реверс"
        )
        self.rotate_clips_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Повернуть"
        )
        self.set_audio_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Установить аудио"
        )
        self.swap_clips_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Поменять местами"
        )
        self.split_fragment_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Разделить фрагмент"
        )
        self.copy_fragment_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Повторить фрагмент"
        )
        self.remove_fragments_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Удалить фрагменты"
        )
        self.preview_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Предпросмотр"
        )
        self.change_speed_button.grid(row=0, column=0, stick="we", padx=10, pady=15)
        self.change_volume_button.grid(row=1, column=0, stick="we", padx=10, pady=15)
        self.concatenate_button.grid(row=2, column=0, stick="we", padx=10, pady=15)
        self.crop_clip_button.grid(row=3, column=0, stick="we", padx=10, pady=15)
        self.crop_picture_button.grid(row=0, column=1, stick="we", padx=10, pady=15)
        self.fade_in_button.grid(row=1, column=1, stick="we", padx=10, pady=15)
        self.fade_out_button.grid(row=2, column=1, stick="we", padx=10, pady=15)
        self.remove_audio_button.grid(row=3, column=1, stick="we", padx=10, pady=15)
        self.reverse_button.grid(row=0, column=2, stick="we", padx=10, pady=15)
        self.rotate_clips_button.grid(row=1, column=2, stick="we", padx=10, pady=15)
        self.set_audio_button.grid(row=2, column=2, stick="we", padx=10, pady=15)
        self.swap_clips_button.grid(row=3, column=2, stick="we", padx=10, pady=15)
        self.split_fragment_button.grid(row=0, column=3, stick="we", padx=10, pady=15)
        self.copy_fragment_button.grid(row=1, column=3, stick="we", padx=10, pady=15)
        self.remove_fragments_button.grid(row=2, column=3, stick="we", padx=10, pady=15)
        self.preview_button.grid(row=3, column=3, stick="we", padx=10, pady=15)

        self.button_time_line = ButtonTimeLine(self, self.time_line)

    def run(self):
        self.window.mainloop()

    def undo_command_handler(self):
        if len(self.time_line.changes) == 0:
            self.show_error("В данный момент отменять нечего")
            return
        self.time_line.undo()
        self.update_after_command()

    def upload_video_handler(self):
        video_path = filedialog.askopenfilename()
        if video_path == "":
            return
        if not video_path.endswith(".mp4"):
            self.show_error("Файл должен быть с расширением .mp4")
            return
        clip = mp.VideoFileClip(video_path)
        fragment = Fragment(clip, len(self.time_line.time_line), video_path)
        self.time_line.add(fragment)
        self.update_after_command()

    def export_handler(self):
        if len(self.time_line.time_line) == 0:
            self.show_error("Пока что нечего сохранять")
            return
        export_path = filedialog.asksaveasfilename(defaultextension=".mp4")

        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("500x200")
        dialog.resizable(False, False)
        label_fps = Label(dialog, text="Введите fps")
        label_fps.grid(row=0, column=0)
        input_field = Entry(dialog)
        input_field.grid(row=0, column=1)
        label_res = Label(dialog, text="Введите разрешение (ширина x высота)")
        res_input_1 = Entry(dialog)
        res_input_2 = Entry(dialog)
        x_label = Label(dialog, text="x")
        label_res.grid(row=1, column=0)
        res_input_1.grid(row=1, column=1)
        x_label.grid(row=1, column=2)
        res_input_2.grid(row=1, column=3)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_export(dialog, export_path,
                                                                input_field.get(),
                                                                res_input_1.get(),
                                                                res_input_2.get()))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.grid(row=2, column=2)
        cancel_button.grid(row=2, column=3)

    def apply_export(self, dialog, name, fps, width, height):
        if not (fps.isdigit() and width.isdigit() and height.isdigit() and int(fps) > 0 and int(width) > 0 and int(height) > 0):
            self.show_error("fps и разрешение должны быть натуральными числами")
            return
        self.time_line.export(name, int(fps), int(width), int(height))
        dialog.destroy()

    def upload_image_handler(self):
        pass

    def update_after_command(self):
        self.button_time_line.update()
        self.toggle_buttons()

    def toggle_buttons(self):
        if len(self.picked_indexes) == 0:
            pass
        elif len(self.picked_indexes) == 1:
            pass
        else:
            pass

    def show_error(self, error_text):
        messagebox.showerror("Ошибка", error_text)
