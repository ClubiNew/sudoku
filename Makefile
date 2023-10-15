install:
	pip install -r requirements.txt

tests:
	python -m nose2

all: install tests

.PHONY: all install tests
.DEFAULT_GOAL := all
