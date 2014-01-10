all:

test:
	python test.py
	python3 test.py

clean:
	find | egrep '.pyc$$|.swp$$|.ly$$|.pdf$$|.midi$$' | xargs -n1 rm -fv
	find | grep __pycache__ | xargs -n1 rm -rfv

tree:
	find | grep -v '/\.'

