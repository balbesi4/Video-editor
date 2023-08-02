from CommandInterface import CommandInterface
from Fragment import Fragment


class AddCommand(CommandInterface):
    def __init__(self, time_line, fragment: Fragment):
        self.time_line = time_line
        self.fragment = fragment

    def execute(self):
        self.time_line.time_line.insert(self.fragment.id, self.fragment)
        self.time_line.update_ids()

    def undo(self):
        self.time_line.time_line.remove(self.fragment)
        self.time_line.update_ids()