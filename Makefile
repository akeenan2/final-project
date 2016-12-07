test: test-mapper test-reducer test-sort test-master

test-mapper:
	@echo Testing mapper...
	@diff --suppress-common-lines -y <(./test/mapper_test.py | sort) data/mapper_output.txt

test-reducer:
	@echo Testing reducer...
	@diff --suppress-common-lines -y <(./test/reducer_test.py | sort) data/reducer_output.txt

test-sort:
	@echo Testing sort...
	@diff --suppress-common-lines -y <(./test/sort_test.py | sort) data/sort_output.txt

test-master:
	@echo Testing master...
	@diff --suppress-common-lines -y <(./test/master_test.py | sort) data/master_output.txt
