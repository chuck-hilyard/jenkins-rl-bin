
default :
	python3 cmr/cmr-approval-gate

tests :
	python3 -m unittest discover

clean :
	rm -f test.txt

