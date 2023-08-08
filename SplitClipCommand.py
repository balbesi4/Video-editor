from CommandInterface import CommandInterface
from Fragment import Fragment


class SplitClipCommand(CommandInterface):
    def __str__(self):
        return f"Разделение фрагмента {self.fragment.id + 1} на 2 фрагмента по {self.split_time} секунде"

    def __init__(self, time_line, fragment: Fragment, split_time):
        self.time_line = time_line
        self.split_time = split_time
        self.fragment = fragment
        self.new_fr_1 = None
        self.new_fr_2 = None

    def execute(self):
        clip_1 = self.fragment.clip.subclip(0, self.split_time)
        clip_2 = self.fragment.clip.subclip(self.split_time, self.fragment.clip.duration)
        self.new_fr_1 = Fragment(clip_1, self.fragment.id, self.fragment.path)
        self.new_fr_2 = Fragment(clip_2, self.fragment.id + 1, self.fragment.path)
        self.time_line.time_line.remove(self.fragment)
        self.time_line.time_line.insert(self.new_fr_1.id, self.new_fr_1)
        self.time_line.time_line.insert(self.new_fr_2.id, self.new_fr_2)

    def undo(self):
        self.time_line.time_line.remove(self.new_fr_1)
        self.time_line.time_line.remove(self.new_fr_2)
        self.time_line.time_line.insert(self.fragment.id, self.fragment)