from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.video.fx.all as vfx


class ChangeSpeedCommand(CommandInterface):
    def __init__(self, time_line, speed_multiplier, fragment: Fragment):
        self.sm = speed_multiplier
        self.fragment = fragment
        self.time_line = time_line

    def execute(self):
        changed_clip = self.fragment.clip.fx(vfx.speedx, self.sm)
        self.time_line.time_line[self.fragment.id].set_clip(changed_clip)

    def undo(self):
        old_clip = self.fragment.clip.fx(vfx.speedx, 1 / self.sm)
        self.time_line.time_line[self.fragment.id].set_clip(old_clip)
