from CommandInterface import CommandInterface
from Fragment import Fragment


class SwapClipsCommand(CommandInterface):
    def __str__(self):
        return f"Смена клипов {self.fragment_1.id + 1} и {self.fragment_2.id + 1} местами"

    def __init__(self, time_line, fr_1: Fragment, fr_2: Fragment):
        self.time_line = time_line
        self.fragment_1 = fr_1
        self.fragment_2 = fr_2

    def execute(self):
        self.time_line.time_line.remove(self.fragment_1)
        self.time_line.time_line.remove(self.fragment_2)
        self.fragment_1.id, self.fragment_2.id = self.fragment_2.id, self.fragment_1.id
        self.time_line.time_line.insert(self.fragment_1.id, self.fragment_1)
        self.time_line.time_line.insert(self.fragment_2.id, self.fragment_2)

    def undo(self):
        self.execute()
