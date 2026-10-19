.PHONY: calc test all

calc:
	python3 calc/model.py
	python3 calc/model.py calc/scenarios/prototype_moose_v1.json calc/out_prototype_v1

test:
	python3 -m unittest discover -s tests -v

all: calc test
