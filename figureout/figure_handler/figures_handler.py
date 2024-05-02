import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from typing import Union
from tkinter import Tk, filedialog
from pathlib import Path


class FigureHandler:
    def __init__(self):
        self.figures = {}

    def save_fig_pickle(self, fig: Figure, filename: str):
        with open(f"{filename}.mpl", "wb") as file:
            pickle.dump(fig, file)
        fig.savefig(f"{filename}.png")  # Save as PNG as well
        self.figures[filename] = fig

    def show_fig_pickle(self, filepath: Union[str, Path]):
        with open(filepath, "rb") as file:
            fig_handle: Figure = pickle.load(file)
        plt.figure(fig_handle.number)
        plt.show()
        self.figures[filepath] = fig_handle

    def open_gui(self):
        root = Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(
            title="Open Figure", filetypes=[("Matplotlib Figure", "*.mpl")]
        )
        if file_path:
            self.show_fig_pickle(file_path)
        root.mainloop()


# Example usage:
if __name__ == "__main__":
    # Create an instance of FigureHandler
    handler = FigureHandler()

    # Save a figure
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    print("SAVE FIGURE")
    handler.save_fig_pickle(fig, "example_figure")

    print("Show a saved figure")
    handler.show_fig_pickle("example_figure.mpl")
    plt.show()
    # Open GUI for browsing and opening saved figures
    handler.open_gui()

