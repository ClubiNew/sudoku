install:
	pip install -r requirements.txt

test:
	python -m nose2

exe:
	pyinstaller -F -n sudoku src\gui.py

.PHONY: install test exe
