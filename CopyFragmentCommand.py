from CommandInterface import CommandInterface
from Fragment import Fragment


class CopyFragmentCommand(CommandInterface):
    def __init__(self, time_line, fragment: Fragment):
        self.time_line = time_line
        self.fragment = fragment
        self.new_fragment = None

    def execute(self):
        self.new_fragment = Fragment(self.fragment.clip.copy(), self.fragment.id + 1, self.fragment.path)
        self.time_line.add(self.new_fragment)

    def undo(self):
        self.time_line.remove(self.new_fragment)