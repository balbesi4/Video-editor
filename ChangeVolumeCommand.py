from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.audio.fx.all as afx


class ChangeVolumeCommand(CommandInterface):
    def __init__(self, time_line, volume_multiplier, fragment: Fragment):
        self.vm = volume_multiplier
        self.fragment = fragment
        self.time_line = time_line

    def execute(self):
        changed_clip = self.fragment.clip.fx(afx.volumex, self.vm)
        self.time_line.time_line[self.fragment.id].set_clip(changed_clip)

    def undo(self):
        old_clip = self.fragment.clip.fx(afx.volumex, 1 / self.vm)
        self.time_line.time_line[self.fragment.id].set_clip(old_clip)
