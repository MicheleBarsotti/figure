# FigureOut

FigureOut is a Python package for handling figures in a convenient and efficient manner. It provides classes and functions for saving, loading, and displaying Matplotlib figures.

## Installation

You can install FigureOut using pip:

```bash
pip install figureout
```

## Usage

### Saving Figures

```python
import matplotlib.pyplot as plt
from figureout.figure_handler import FigureHandler

# Create a figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Save the figure
handler = FigureHandler()
handler.save_fig_pickle(fig, "example_figure")
```

### Loading and Displaying Figures

```python
# Load and display a saved figure
handler.show_fig_pickle("example_figure.mpl")
```

### GUI for Browsing and Opening Figures

```python
# Open GUI for browsing and opening saved figures
handler.open_gui()
```

## Dependencies

- Python (>=3.8,<3.9)
- Matplotlib (>=3.0.0)

## License

This project is licensed under the MIT License 

