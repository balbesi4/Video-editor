from GUI import GraphicalUserInterface
import atexit


gui = GraphicalUserInterface()
gui.run()


def exit_handler():
    global gui
    gui.exit_handler()


atexit.register(exit_handler)
