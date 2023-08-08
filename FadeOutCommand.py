from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx


class FadeOutCommand(CommandInterface):
    def __str__(self):
        return f"Fade out во фрагменте {self.fragment.id + 1}"

    def __init__(self, time_line, duration, fragment: Fragment):
        self.duration = duration
        self.old_clip = fragment.clip
        self.time_line = time_line
        self.fragment = fragment

    def execute(self):
        new_clip = self.fragment.clip.fx(vfx.fadeout, self.duration)
        if new_clip.audio is not None:
            audio = new_clip.audio.fx(afx.audio_fadein, self.duration)
            new_clip.audio = audio
        self.time_line.time_line[self.fragment.id].set_clip(new_clip)

    def undo(self):
        self.time_line.time_line[self.fragment.id].set_clip(self.old_clip)
