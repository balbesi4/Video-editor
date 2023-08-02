import moviepy.editor as mp
import os


class Fragment:
    def __init__(self, clip: mp.VideoClip, fr_id: int, path):
        self.clip = clip
        self.id = fr_id
        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]

    def set_clip(self, clip: mp.VideoClip):
        self.clip = clip
