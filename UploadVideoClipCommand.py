from CommandInterface import CommandInterface
from Fragment import Fragment
import moviepy.editor as mp


class UploadVideoClipCommand(CommandInterface):
    def __init__(self, time_line, path: str):
        self.time_line = time_line
        self.fragment = Fragment(mp.VideoFileClip(path), time_line.count(), path)

    def execute(self):
        self.time_line.add(self.fragment)

    def undo(self):
        self.time_line.remove(self.fragment)
