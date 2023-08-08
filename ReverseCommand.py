from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx


class ReverseCommand(CommandInterface):
    def __str__(self):
        return f"Реверс клипа фрагмента {self.fragment.id + 1}"

    def __init__(self, fragment: Fragment):
        self.fragment = fragment

    def execute(self):
        duration = self.fragment.clip.duration
        video = self.fragment.clip.fl_time(lambda t: duration - t, apply_to=['mask', 'audio']).set_duration(duration)
        self.fragment.clip = video

    def undo(self):
        self.execute()
