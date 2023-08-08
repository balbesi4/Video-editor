from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.editor as mp


class SetAudioCommand(CommandInterface):
    def __str__(self):
        return f"Установка аудио во фрагменте {self.fragment.id + 1}"

    def __init__(self, time_line, audio_path, fragment: Fragment, full=False):
        self.time_line = time_line
        self.new_audio = mp.AudioFileClip(audio_path)
        self.old_audio = fragment.clip.audio
        if full:
            multiplier = self.new_audio.duration / fragment.clip.duration
            full_audio = self.new_audio.fl_time(lambda t: multiplier * t,
                                                apply_to=['mask', 'audio'])
            full_audio.duration = self.new_audio.duration / multiplier
            self.new_audio = full_audio
        else:
            self.new_audio.duration = min(self.new_audio.duration, fragment.clip.duration)
        self.fragment = fragment

    def execute(self):
        self.fragment.clip.audio = self.new_audio

    def undo(self):
        self.fragment.clip.audio = self.old_audio
