from CommandInterface import CommandInterface
from Fragment import Fragment


class RotateClipsCommand(CommandInterface):
    def __str__(self):
        fr_str = ""
        for fragment in self.fragments:
            fr_str += f"{fragment.id + 1}, "
        fr_str = fr_str[:-1]
        return f"Поворот клипов фрагментов {fr_str} на {self.angle} градусов"

    def __init__(self, *fragments: Fragment, angle):
        self.fragments = fragments
        self.angle = angle

    def execute(self):
        for fragment in self.fragments:
            new_clip = fragment.clip.rotate(self.angle)
            fragment.clip = new_clip

    def undo(self):
        for fragment in self.fragments:
            new_clip = fragment.clip.rotate(180 - self.angle)
            fragment.clip = new_clip