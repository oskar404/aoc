# Makefile for AOC development

all: lint test

lint:
	black *.py
	flake8 *.py
	pylint *.py
	mypy *.py

test:
	pytest

clean:
	@rm -f __pycache__ *~ *.pyc

.PHONY: lint clean
