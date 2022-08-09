import tkinter
from tkinter import BOTH


class paper:
    tk = None
    def __init__(self, width = 600, height = 600):
        # Set some attributes
        paper.tk.title("Drawing shapes")
        paper.tk.geometry(str(width) + "x" + str(height))
        paper.tk.paper_width = width
        paper.tk.paper_height = height

        # Create a tkinter canvas object to draw on
        paper.tk.canvas = tkinter.Canvas(paper.tk)
        paper.tk.canvas.pack(fill=BOTH, expand=1)

