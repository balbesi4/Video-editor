import moviepy.editor as mp
import re
from tkinter import messagebox, filedialog
from ButtonTimeLine import ButtonTimeLine
from Fragment import Fragment
from TimeLine import TimeLine
from tkinter import *
from PIL import Image, ImageTk
import moviepy.video.fx.all as vfx


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
        self.main_frame.grid_columnconfigure(0, minsize=200)
        self.main_frame.grid_columnconfigure(1, minsize=100)

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
            bg="#938CDD",
            command=lambda: self.upload_image_handler()
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
            command=lambda: self.undo_command_handler()
        )
        self.change_story_button = Button(
            self.main_frame,
            height=2,
            font=("Noto Sans Symbols 2", 12),
            text="🕒",
            bg="#938CDD",
            command=lambda: self.story_changes_handler()
        )
        self.upload_video_button.grid(row=0, column=0, columnspan=2, stick="we", padx=25, pady=12)
        self.upload_image_button.grid(row=1, column=0, columnspan=2, stick="we", padx=25, pady=12)
        self.export_button.grid(row=2, column=0, columnspan=2, stick="we", padx=25, pady=12)
        self.undo_button.grid(row=3, column=0, stick="we", padx=25, pady=12)
        self.change_story_button.grid(row=3, column=1, stick="we", padx=25, pady=12)

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
            text="Изменить скорость",
            command=lambda: self.change_speed_handler()
        )
        self.change_volume_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Изменить громкость",
            command=lambda: self.change_volume_handler()
        )
        self.concatenate_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Склеить фрагменты",
            command=lambda: self.concatenate_handler()
        )
        self.crop_clip_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Обрезать фрагмент",
            command=lambda: self.crop_clip_handler()
        )
        self.crop_picture_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Кроп картинки",
            command=lambda: self.crop_picture_handler()
        )
        self.fade_in_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Fade in",
            command=lambda: self.fade_in_handler()
        )
        self.fade_out_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Fade out",
            command=lambda: self.fade_out_handler()
        )
        self.remove_audio_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Убрать аудио",
            command=lambda: self.remove_audio_handler()
        )
        self.reverse_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Реверс",
            command=lambda: self.reverse_handler()
        )
        self.rotate_clips_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Повернуть",
            command=lambda: self.rotate_clip_handler()
        )
        self.set_audio_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Установить аудио",
            command=lambda: self.set_audio_handler()
        )
        self.swap_clips_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Поменять местами",
            command=lambda: self.swap_clips_handler()
        )
        self.split_fragment_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Разделить фрагмент",
            command=lambda: self.split_fragment_handler()
        )
        self.copy_fragment_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Повторить фрагмент",
            command=lambda: self.copy_fragment_handler()
        )
        self.remove_fragments_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Удалить фрагменты",
            command=lambda: self.remove_fragments_handler()
        )
        self.mirror_button = Button(
            self.command_frame,
            font=self.main_font,
            bg="#938CDD",
            text="Отзеркалить картинку",
            command=lambda: self.mirror_handler()
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
        self.mirror_button.grid(row=3, column=3, stick="we", padx=10, pady=15)

        self.one_button_commands = [self.change_speed_button, self.change_volume_button,
                                    self.crop_clip_button, self.fade_in_button,
                                    self.fade_out_button, self.set_audio_button,
                                    self.crop_picture_button, self.reverse_button,
                                    self.split_fragment_button, self.copy_fragment_button,
                                    self.remove_fragments_button, self.remove_audio_button,
                                    self.rotate_clips_button, self.mirror_button]
        self.two_button_commands = [self.concatenate_button, self.swap_clips_button,
                                    self.rotate_clips_button, self.remove_audio_button,
                                    self.remove_fragments_button]
        self.many_button_commands = [self.concatenate_button, self.rotate_clips_button,
                                     self.remove_audio_button, self.remove_fragments_button]

        self.button_time_line = ButtonTimeLine(self, self.time_line)
        self.toggle_buttons()

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

        self.time_line.upload_video(video_path)
        self.update_after_command()

    def export_handler(self):
        if len(self.time_line.time_line) == 0:
            self.show_error("Пока что нечего сохранять")
            return

        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("500x130")
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
        ext_label = Label(dialog, text="Выберите расширение")
        ext_label.grid(row=2, column=0)
        save_var = StringVar()
        save_var.set("файл .mp4")
        option_menu = OptionMenu(dialog, save_var, "файл .mp4", "файл .gif")
        option_menu.grid(row=2, column=1, columnspan=3, stick="we")
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_export(dialog,
                                                                input_field.get(),
                                                                res_input_1.get(),
                                                                res_input_2.get(),
                                                                save_var.get()))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=350, y=100)
        cancel_button.place(x=420, y=100)

    def apply_export(self, dialog, fps, width, height, save_result):
        if not (fps.isdigit() and width.isdigit() and height.isdigit() and int(fps) > 0 and int(
                width) > 0 and int(height) > 0):
            self.show_error("fps и разрешение должны быть натуральными числами")
            return
        gif = save_result == "файл .gif"
        if gif:
            export_path = filedialog.asksaveasfilename(defaultextension=".gif")
        else:
            export_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        if export_path == "":
            return
        dialog.destroy()
        self.time_line.export(export_path, int(fps), int(width), int(height), gif)

    def upload_image_handler(self):
        image_path = filedialog.askopenfilename()
        if image_path == "":
            return
        if not (image_path.endswith(".jpeg") or image_path.endswith(".png") or image_path.endswith(
                ".tiff") or image_path.endswith(".jpg")):
            self.show_error("Файл должен быть с расширениями .jpeg, .jpg, .png или .tiff")
            return

        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        duration_label = Label(dialog, text="Введите продолжительность")
        duration_label.grid(row=0, column=0)
        duration_entry = Entry(dialog)
        duration_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_upload_image(duration_entry.get(),
                                                                      image_path, dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_upload_image(self, duration, image_path, dialog):
        if not re.match(r"^([0-9]|[1-9][0-9]*)\.?[0-9]*$", duration):
            self.show_error("Длительность должна быть положительным числом")
            return

        dialog.destroy()
        self.time_line.upload_image(image_path, float(duration))
        self.update_after_command()

    def story_changes_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.resizable(False, False)
        dialog.geometry("680x200")
        frame = Frame(dialog)
        canvas = Canvas(frame)
        vertical_scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vertical_scrollbar.set)
        label_text = ""
        command_count = 0
        for command in self.time_line.changes:
            label_text += f"{command_count + 1}. {str(command)}\n"
            command_count += 1
        if command_count == 0:
            label_text = "История изменений на данный момент пуста"
        else:
            label_text = label_text[:-1]

        label = Label(canvas, text=label_text, font=("Roboto", 14), compound=LEFT, anchor="nw")
        canvas.create_window(0, 0, anchor="nw", window=label)
        canvas.pack(side="left", fill="both", expand=True)
        vertical_scrollbar.pack(side="right", fill="y")
        canvas.config(scrollregion=canvas.bbox("all"))
        frame.pack(fill="both", expand=True)

    def change_speed_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        multiplier_label = Label(dialog, text="Введите множитель скорости")
        multiplier_label.grid(row=0, column=0)
        multiplier_entry = Entry(dialog)
        multiplier_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_speed_change(multiplier_entry.get(),
                                                                      dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_speed_change(self, multiplier, dialog):
        if not re.match(r"^[1-9][0-9]*\.?[0-9]*$", multiplier):
            self.show_error("Множитель должен быть положительным числом")
            return

        dialog.destroy()
        self.time_line.change_speed(float(multiplier), self.picked_indexes[0])
        self.update_after_command()

    def change_volume_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        multiplier_label = Label(dialog, text="Введите множитель громкости")
        multiplier_label.grid(row=0, column=0)
        multiplier_entry = Entry(dialog)
        multiplier_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_volume_change(multiplier_entry.get(),
                                                                       dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_volume_change(self, multiplier, dialog):
        if not re.match(r"^[1-9][0-9]*\.?[0-9]*$", multiplier):
            self.show_error("Множитель должен быть положительным числом")
            return

        dialog.destroy()
        self.time_line.change_volume(float(multiplier), self.picked_indexes[0])
        self.update_after_command()

    def concatenate_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x100")
        dialog.resizable(False, False)
        smooth_label = Label(dialog, text="Плавный переход")
        smooth_label.grid(row=0, column=0)
        smooth_var = BooleanVar()
        smooth_checkbox = Checkbutton(dialog, variable=smooth_var,
                                      command=lambda: self.on_smooth_checkbox_click(smooth_var,
                                                                                    duration_entry))
        smooth_checkbox.grid(row=0, column=1)
        duration_label = Label(dialog, text="Введите длительность перехода")
        duration_label.grid(row=1, column=0)
        duration_entry = Entry(dialog, state=DISABLED)
        duration_entry.grid(row=1, column=1)

        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_concatenate(smooth_var.get(),
                                                                     duration_entry.get(),
                                                                     dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=70)
        cancel_button.place(x=220, y=70)

    def on_smooth_checkbox_click(self, smooth_var, duration_entry):
        if smooth_var.get():
            duration_entry.configure(state=NORMAL)
        else:
            duration_entry.configure(state=DISABLED)

    def apply_concatenate(self, smooth, duration, dialog):
        if smooth and not re.match(r"^[1-9][0-9]*\.?[0-9]*$", duration):
            self.show_error("Длительность должна быть положительным числом")
            return
        elif not smooth:
            duration = 0
        dialog.destroy()
        self.time_line.concatenate(*self.picked_indexes, smooth=smooth, duration=float(duration))
        self.update_after_command()

    def crop_clip_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("350x120")
        dialog.resizable(False, False)
        clip = self.time_line.time_line[self.picked_indexes[0]].clip
        info_label = Label(dialog, text=f"Длительность клипа составляет {clip.duration}")
        info_label.grid(row=0, column=0, columnspan=2, pady=5)
        split_label_1 = Label(dialog, text="Введите секунду начала нового клипа")
        split_label_1.grid(row=1, column=0)
        split_entry_1 = Entry(dialog)
        split_entry_1.grid(row=1, column=1)
        split_label_2 = Label(dialog, text="Введите секунду конца нового клипа")
        split_label_2.grid(row=2, column=0)
        split_entry_2 = Entry(dialog)
        split_entry_2.grid(row=2, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_crop_clip(split_entry_1.get(),
                                                                   split_entry_2.get(),
                                                                   clip.duration,
                                                                   dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=200, y=90)
        cancel_button.place(x=270, y=90)

    def apply_crop_clip(self, start, end, clip_duration, dialog):
        if not re.match(r"^[1-9][0-9]*\.?[0-9]*$", start) or \
                not re.match(r"^[1-9][0-9]*\.?[0-9]*$",end) or float(end) > clip_duration:
            self.show_error(f"Начало и конец нового клипа должны быть числами от 0 до {clip_duration}")
            return

        dialog.destroy()
        self.time_line.crop_clip(float(start), float(end), self.picked_indexes[0])
        self.update_after_command()

    def crop_picture_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.resizable(False, False)
        label_width, label_height = 640, 480
        clip = self.time_line.time_line[self.picked_indexes[0]].clip.fx(vfx.resize, width=label_width, height=label_height)
        clip_size = self.time_line.time_line[self.picked_indexes[0]].clip.size
        frame = clip.get_frame(t=0)
        image = Image.fromarray(frame)
        image_tk = ImageTk.PhotoImage(image)
        dialog.geometry(f"{label_width + 200}x{label_height + 200}")
        slider_1 = Scale(dialog, from_=1, to=clip_size[0], orient=HORIZONTAL, width=5, length=label_width)
        slider_2 = Scale(dialog, from_=1, to=clip_size[1], orient=VERTICAL, width=5, length=label_height)
        slider_3 = Scale(dialog, from_=1, to=clip_size[0], orient=HORIZONTAL, width=5, length=label_width)
        slider_4 = Scale(dialog, from_=1, to=clip_size[1], orient=VERTICAL, width=5, length=label_height)
        slider_3.set(clip_size[0])
        slider_4.set(clip_size[1])
        label = Label(dialog, width=label_width, height=label_height)
        label.configure(image=image_tk)
        label.image = image_tk
        label.place(x=100, y=100)
        label_text = Label(dialog, text="Укажите координаты левой верхней и правой нижней точки с помощью слайдеров")
        label_text.pack(side=TOP, pady=20)
        slider_1.place(x=100, y=50)
        slider_2.place(x=50, y=100)
        slider_3.place(x=100, y=label_height + 100)
        slider_4.place(x=label_width + 100, y=100)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_picture_crop(slider_1.get(), slider_2.get(),
                                                                      slider_3.get(), slider_4.get(),
                                                                      dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=690, y=650)
        cancel_button.place(x=760, y=650)

    def apply_picture_crop(self, x1, y1, x2, y2, dialog):
        if x1 > x2 or y1 > y2:
            self.show_error("Левая верхняя точка не может находиться ниже или правее правой нижней")
            return
        dialog.destroy()
        self.time_line.crop_clip_picture(self.picked_indexes[0], float(x1), float(y1), float(x2), float(y2))
        self.update_after_command()

    def fade_in_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        time_label = Label(dialog, text="Введите длительность в секундах")
        time_label.grid(row=0, column=0)
        time_entry = Entry(dialog)
        time_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_fade_in(time_entry.get(), dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_fade_in(self, time, dialog):
        if not re.match(r"^[1-9][0-9]*\.?[0-9]*$", time):
            self.show_error("Длительность должна быть положительным числом")
            return
        dialog.destroy()
        self.time_line.fade_in(self.picked_indexes[0], float(time))
        self.update_after_command()

    def fade_out_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        time_label = Label(dialog, text="Введите длительность в секундах")
        time_label.grid(row=0, column=0)
        time_entry = Entry(dialog)
        time_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_fade_in(time_entry.get(), dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_fade_out(self, time, dialog):
        if not re.match(r"^[1-9][0-9]*\.?[0-9]*$", time):
            self.show_error("Длительность должна быть положительным числом")
            return
        dialog.destroy()
        self.time_line.fade_out(self.picked_indexes[0], float(time))
        self.update_after_command()

    def remove_audio_handler(self):
        self.time_line.remove_audio(*self.picked_indexes)
        self.update_after_command()

    def reverse_handler(self):
        self.time_line.reverse(self.picked_indexes[0])
        self.update_after_command()

    def rotate_clip_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("300x60")
        dialog.resizable(False, False)
        angle_label = Label(dialog, text="Введите угол поворота")
        angle_label.grid(row=0, column=0)
        angle_entry = Entry(dialog)
        angle_entry.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_clip_rotate(angle_entry.get(), dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=150, y=30)
        cancel_button.place(x=220, y=30)

    def apply_clip_rotate(self, angle, dialog):
        if not (angle.isdigit() and 0 < int(angle) < 180):
            self.show_error("Угол должен быть целым числом в диапазоне (0, 180)")
            return
        dialog.destroy()
        self.time_line.rotate_clips(*self.picked_indexes, angle=int(angle))
        self.update_after_command()

    def set_audio_handler(self):
        audio_path = filedialog.askopenfilename()
        if audio_path == "":
            return
        if not audio_path.endswith(".mp3") and not audio_path.endswith(".wav"):
            self.show_error("Файл должен быть с расширением .mp3 или .wav")
            return
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("200x60")
        dialog.resizable(False, False)
        time_label = Label(dialog, text="Растянуть аудио на все видео")
        time_label.grid(row=0, column=0)
        full_var = BooleanVar()
        full_checkbox = Checkbutton(dialog, variable=full_var)
        full_checkbox.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_audio_set(audio_path, full_var.get(), dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=50, y=30)
        cancel_button.place(x=120, y=30)

    def apply_audio_set(self, audio_path, full, dialog):
        dialog.destroy()
        self.time_line.set_audio(audio_path, self.picked_indexes[0], full=full)
        self.update_after_command()

    def swap_clips_handler(self):
        self.time_line.swap_clips(self.picked_indexes[0], self.picked_indexes[1])
        self.update_after_command()

    def mirror_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("220x80")
        dialog.resizable(False, False)
        text_label = Label(dialog, text="Отзеркалить по")
        text_label.grid(row=0, column=0)
        mirror_var = StringVar()
        mirror_var.set("горизонтали")
        option_menu = OptionMenu(dialog, mirror_var, "горизонтали", "вертикали")
        option_menu.grid(row=0, column=1)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_mirror(mirror_var.get(), dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=70, y=50)
        cancel_button.place(x=140, y=50)

    def apply_mirror(self, side, dialog):
        x = side == "горизонтали"
        dialog.destroy()
        self.time_line.mirror(self.picked_indexes[0], x)
        self.update_after_command()

    def split_fragment_handler(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("230x90")
        dialog.resizable(False, False)
        time_label = Label(dialog, text="Введите секунду")
        time_label.grid(row=1, column=0)
        time_entry = Entry(dialog)
        time_entry.grid(row=1, column=1)
        clip_duration = self.time_line.time_line[self.picked_indexes[0]].clip.duration
        text_label = Label(dialog, text=f"Длительность видео {clip_duration}")
        text_label.grid(row=0, column=0, columnspan=2, pady=5)
        apply_button = Button(dialog, text="Готово",
                              command=lambda: self.apply_split_fragment(time_entry.get(), clip_duration, dialog))
        cancel_button = Button(dialog, text="Отменить", command=dialog.destroy)
        apply_button.place(x=80, y=60)
        cancel_button.place(x=150, y=60)

    def apply_split_fragment(self, time, clip_duration, dialog):
        if not (re.match(r"^[1-9][0-9]*\.?[0-9]*$", time) and 0 < float(time) < float(clip_duration)):
            self.show_error(f"Секунда должна быть числом между 0 и {clip_duration}")
            return
        dialog.destroy()
        self.time_line.split_clip(self.picked_indexes[0], float(time))
        self.update_after_command()

    def copy_fragment_handler(self):
        self.time_line.copy_fragment(self.picked_indexes[0])
        self.update_after_command()

    def remove_fragments_handler(self):
        self.time_line.remove(*self.picked_indexes)
        self.update_after_command()

    def update_after_command(self):
        self.button_time_line.update()
        self.picked_indexes.clear()
        self.toggle_buttons()

    def exit_handler(self):
        for fragment in self.time_line.time_line:
            fragment.clip.close()

    def toggle_buttons(self):
        if len(self.picked_indexes) == 0:
            for button in self.one_button_commands + self.two_button_commands + self.many_button_commands:
                button.configure(state=DISABLED)
        elif len(self.picked_indexes) == 1:
            for button in self.one_button_commands:
                button.configure(state=NORMAL)
            for button in self.two_button_commands + self.many_button_commands:
                if button not in self.one_button_commands:
                    button.configure(state=DISABLED)
        elif len(self.picked_indexes) == 2:
            for button in self.two_button_commands:
                button.configure(state=NORMAL)
            for button in self.one_button_commands + self.many_button_commands:
                if button not in self.two_button_commands:
                    button.configure(state=DISABLED)
        else:
            for button in self.many_button_commands:
                button.configure(state=NORMAL)
            for button in self.two_button_commands + self.one_button_commands:
                if button not in self.many_button_commands:
                    button.configure(state=DISABLED)
            pass

    def show_error(self, error_text):
        messagebox.showerror("Ошибка", error_text)
