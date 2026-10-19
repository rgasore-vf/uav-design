.PHONY: calc test all

calc:
	python3 calc/model.py

test:
	python3 -m unittest discover -s tests -v

all: calc test
