test: test-mapper test-reducer test-sort test-master

test-mapper:
	@echo Testing mapper...
	@diff --suppress-common-lines -y <(./test/mapper_test.py | sort) data/mapper_output.txt

test-sort:
	@echo Testing sort...
	@diff --suppress-common-lines -y <(./test/sort_test.py | sort) data/sort_output.txt

test-master:
	@echo Testing master...
	@diff --suppress-common-lines -y <(./test/master_test.py | sort) data/master_output.txt
