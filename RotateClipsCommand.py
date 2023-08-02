from CommandInterface import CommandInterface
from Fragment import Fragment


class RotateClipsCommand(CommandInterface):
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