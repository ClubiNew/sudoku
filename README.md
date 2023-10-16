# sudoku
[![ci](https://github.com/ClubiNew/sudoku/actions/workflows/ci.yml/badge.svg)](https://github.com/ClubiNew/sudoku/actions/workflows/ci.yml) [![cd](https://github.com/ClubiNew/sudoku/actions/workflows/cd.yml/badge.svg)](https://github.com/ClubiNew/sudoku/actions/workflows/cd.yml)

This is a small project for automatically generating and solving sudoku puzzles. It comes with a pygame GUI that allows for easy puzzle entry or generation; and solving manually, with hints, or automatically.

<img src="img/unsolved.jpg" alt="partially solved sudoku puzzle" width="70%">

<img src="img/mistake.jpg" alt="partially solved sudoku puzzle with mistake" width="35%"> <img src="img/solved.jpg" alt="solved sudoku puzzle" width="35%">

## Setup and running

You can download a binary file from the [latest release](https://github.com/ClubiNew/sudoku/releases) or run the code directly:

1. Clone the repository
2. Ensure you have Python 3.12 installed
3. Run `make install` to retrieve pip dependencies
4. Run [src/gui.py](src/gui.py) to launch the graphical interface

Controls and other information can be found within the GUI.
