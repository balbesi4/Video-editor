import imageio
import visvis as vv
from Fragment import Fragment
from GUI import GraphicalUserInterface
import atexit
from TimeLine import TimeLine
import moviepy.editor as mp
import moviepy.video.fx.all as vfx


gui = GraphicalUserInterface()
gui.run()


def exit_handler():
    global gui
    gui.exit_handler()


atexit.register(exit_handler)
