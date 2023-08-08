from CommandInterface import CommandInterface
from Fragment import Fragment


class CropClipCommand(CommandInterface):
    def __str__(self):
        return f"Обрезание клипа фрагмента {self.fragment.id + 1} с {self.start} секунды до {self.end} секунды"

    def __init__(self, time_line, crop_start, crop_end, fragment: Fragment):
        self.time_line = time_line
        self.start = crop_start
        self.end = crop_end
        self.old_clip = fragment.clip
        self.fragment = fragment

    def execute(self):
        changed_clip = self.fragment.clip.subclip(self.start, self.end)
        self.time_line.time_line[self.fragment.id].set_clip(changed_clip)

    def undo(self):
        self.time_line.time_line[self.fragment.id].set_clip(self.old_clip)
