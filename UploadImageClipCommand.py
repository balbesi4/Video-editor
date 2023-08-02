from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.editor as mp


class UploadImageClipCommand(CommandInterface):
    def __init__(self, time_line, path: str, duration):
        self.time_line = time_line
        clip = mp.ImageClip(path, duration=duration)
        self.fragment = Fragment(clip, time_line.count(), path)

    def execute(self):
        self.time_line.add(self.fragment)

    def undo(self):
        self.time_line.remove(self.fragment)
