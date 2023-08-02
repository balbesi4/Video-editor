from CommandInterface import CommandInterface
from Fragment import Fragment
from moviepy.video.fx.all import crop


class CropPictureCommand(CommandInterface):
    def __init__(self, fragment: Fragment, x1=0, y1=0, x2=0, y2=0):
        self.fragment = fragment
        self.old_clip = fragment.clip
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def execute(self):
        new_clip = crop(self.fragment.clip, x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y2)
        self.fragment.clip = new_clip

    def undo(self):
        self.fragment.clip = self.old_clip
