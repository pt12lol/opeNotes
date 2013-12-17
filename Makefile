all:

test:
	python3 test.py

clean:
	find | grep \'\.pyc$\' | xargs -n1 rm

tree:
	find | grep -v '/\.'

