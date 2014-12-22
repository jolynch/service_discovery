.PHONY: all production web cmd test tests clean

all: production

production:
	@true

tests: test

test:
	tox

clean:
	rm -rf service_discovery.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
