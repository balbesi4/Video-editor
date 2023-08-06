from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.video.fx.all as vfx


class ReverseCommand(CommandInterface):
    def __init__(self, fragment: Fragment):
        self.fragment = fragment

    def execute(self):
        self.fragment.clip = self.fragment.clip.fx(vfx.mirror_x)

    def undo(self):
        self.execute()
