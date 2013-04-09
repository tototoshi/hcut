.PHONY: test
test:
	PYTHONPATH=.:$$PYTHONPATH bin/hcut -f USER_ID -f NAME test/a.txt test/b.txt
	PYTHONPATH=.:$$PYTHONPATH bin/hcut -f USER_ID -f NAME -d ',' test/c.txt
	cat test/a.txt | PYTHONPATH=.:$$PYTHONPATH bin/hcut -f USER_ID -f NAME --header