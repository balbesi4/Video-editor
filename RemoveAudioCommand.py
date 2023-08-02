from CommandInterface import CommandInterface
from Fragment import Fragment


class RemoveAudioCommand(CommandInterface):
    def __init__(self, *fragments: Fragment):
        self.fragments = fragments
        self.old_audios = [fragment.clip.audio for fragment in fragments]

    def execute(self):
        for fragment in self.fragments:
            fragment.clip.set_audio(None)

    def undo(self):
        for i in range(len(self.fragments)):
            self.fragments[i].clip.set_audio(self.old_audios[i])
