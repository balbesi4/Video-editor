from CommandInterface import CommandInterface
from Fragment import Fragment


class RemoveAudioCommand(CommandInterface):
    def __str__(self):
        fr_str = ""
        for fragment in self.fragments:
            fr_str += f"{fragment.id + 1}, "
        fr_str = fr_str[:-1]
        return f"Удаление аудио во фрагментах {fr_str}"

    def __init__(self, *fragments: Fragment):
        self.fragments = fragments
        self.old_audios = [fragment.clip.audio for fragment in fragments]

    def execute(self):
        for fragment in self.fragments:
            fragment.clip.audio = None

    def undo(self):
        for i in range(len(self.fragments)):
            self.fragments[i].clip.audio = self.old_audios[i]
