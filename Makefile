
default :
	python3 cmr_approval_gate/main.py

tests :
	python3 -m unittest discover

clean :
	rm -f test.txt

