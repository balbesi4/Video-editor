from CommandInterface import CommandInterface
from Fragment import Fragment


class RemoveFragmentCommand(CommandInterface):
    def __init__(self, time_line, fragment: Fragment):
        self.fragment = fragment
        self.time_line = time_line

    def execute(self):
        self.time_line.time_line.remove(self.fragment)
        self.time_line.update_ids()

    def undo(self):
        self.time_line.time_line.insert(self.fragment.id, self.fragment)
        self.time_line.update_ids()