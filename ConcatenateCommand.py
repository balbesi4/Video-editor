from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx


class ConcatenateCommand(CommandInterface):
    def __str__(self):
        fr_str = ""
        for fragment in self.fragments:
            fr_str += f"{fragment.id + 1}, "
        fr_str = fr_str[:-1]
        return f"Склеивание фрагментов {fr_str}"

    def __init__(self, time_line, *fragments: Fragment, smooth=False, duration=None):
        self.time_line = time_line
        self.fragments = fragments
        self.final_fragment = None
        self.duration = duration
        self.smooth = smooth

    def execute(self):
        if self.smooth:
            self._make_smooth_concat()
        else:
            self._make_default_concat()
        for fragment in self.fragments:
            self.time_line.remove(fragment)
        self.time_line.time_line.insert(self.final_fragment.id, self.final_fragment)

    def _make_smooth_concat(self):
        clips = [fragment.clip for fragment in self.fragments]
        final_clips = []
        for i in range(len(clips)):
            clip = clips[i]
            if i == 0:
                new_clip = clip.fx(vfx.fadeout, self.duration)
                if new_clip.audio is not None:
                    audio = new_clip.audio.fx(afx.audio_fadeout, self.duration)
                    new_clip.audio = audio
            elif i == len(clips) - 1:
                new_clip = clip.fx(vfx.fadein, self.duration)
                if new_clip.audio is not None:
                    audio = new_clip.audio.fx(afx.audio_fadein, self.duration)
                    new_clip.audio = audio
            else:
                new_clip = clip.fx(vfx.fadein, self.duration).fx(vfx.fadeout, self.duration)
                if new_clip.audio is not None:
                    audio = new_clip.audio.fx(afx.audio_fadein, self.duration).fx(afx.audio_fadeout, self.duration)
                    new_clip.audio = audio
            final_clips.append(new_clip)
        result = mp.concatenate_videoclips(final_clips)
        self._initialize_new_fragment(result)

    def _make_default_concat(self):
        clips = [fragment.clip for fragment in self.fragments]
        concatenated_clip = mp.concatenate_videoclips(clips)
        self._initialize_new_fragment(concatenated_clip)

    def _initialize_new_fragment(self, clip: mp.VideoClip):
        first_fragment = self.fragments[0]
        self.final_fragment = Fragment(clip, first_fragment.id, first_fragment.path)

    def undo(self):
        self.time_line.remove(self.final_fragment)
        for fragment in self.fragments:
            self.time_line.time_line.insert(fragment.id, fragment)
