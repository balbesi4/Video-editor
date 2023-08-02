from CommandInterface import CommandInterface
from Fragment import Fragment


class SwapClipsCommand(CommandInterface):
    def __init__(self, time_line, fr_1: Fragment, fr_2: Fragment):
        self.time_line = time_line
        self.fragment_1 = fr_1
        self.fragment_2 = fr_2

    def execute(self):
        self.time_line.remove(self.fragment_1)
        self.time_line.remove(self.fragment_2)
        self.fragment_1.id, self.fragment_2.id = self.fragment_2.id, self.fragment_1.id
        self.time_line.add(self.fragment_1)
        self.time_line.add(self.fragment_2)

    def undo(self):
        self.execute()
