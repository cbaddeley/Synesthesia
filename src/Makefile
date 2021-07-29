# Simple Makefile


build:
	python3 setup.py sdist && pip install ./dist/synesthesia-uf-0.1.11.tar.gz
pkg: 
	python3 setup.py sdist && twine upload dist/*

clean:
	rm -r dist build synesthesia_uf.egg-infoSynesthesiaUF