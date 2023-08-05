from CommandInterface import CommandInterface
from Fragment import Fragment


class RemoveFragmentCommand(CommandInterface):
    def __init__(self, time_line, *fragment_ids: int):
        self.fragments = [fragment for fragment in time_line.time_line if fragment.id in fragment_ids]
        self.time_line = time_line

    def execute(self):
        for fragment in self.fragments:
            self.time_line.time_line.remove(fragment)
        self.time_line.update_ids()

    def undo(self):
        for fragment in self.fragments:
            self.time_line.time_line.insert(fragment.id, fragment)
        self.time_line.update_ids()