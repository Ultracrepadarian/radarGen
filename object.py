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

class Shape:

    def __init__(self, width=50, height=50, x=None, y=None, color=black):
        """
        Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and colour.

        Args:
            width (int): The width of the shape. Defaults to 50.
            height (int): The height of the shape. Defaults to 50.
            x (int): The x position of the shape. If None, the x position will be the middle of the screen. Defaults to None.
            y (int): The y position of the shape. If None, the y position will be the middle of the screen. Defaults to None.
            color (string): The color of the shape. Defaults to "black"
        """
        if Paper.tk is None:
            raise Exception("A Paper object has not been created. There is nothing to draw on.")

        #Set some attributes
        self.height = height
        self.width = width
        self.color = color

        #Put the shape in the centre if no xy coords were given
        if x is None:
            self.x = (Paper.tk.paper_width/2) - (self.width/2)
        else:
            slef.x = x
        if y is None:
            self.y = (Paper.tk.paper_height/2) - (self.height/2)
        else:
            self.y = y

