from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.video.fx.all as vfx


class MirrorCommand(CommandInterface):
    def __init__(self, x, fragment: Fragment):
        self.fragment = fragment
        self.x = x

    def execute(self):
        if self.x:
            self.fragment.clip = self.fragment.clip.fx(vfx.mirror_x)
        else:
            self.fragment.clip = self.fragment.clip.fx(vfx.mirror_y)

    def undo(self):
        self.execute()
