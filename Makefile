install:
	pip install -r requirements.txt

test:
	python -m nose2

all: install test

.PHONY: all install test
.DEFAULT_GOAL := all
