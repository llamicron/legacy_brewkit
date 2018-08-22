clean:
	rm -rf dist/*

build:
	python setup.py sdist

install: clean build
	pip uninstall brewkit -y
	pip install dist/*
	pip list | grep brewkit
