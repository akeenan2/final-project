test: test-mapper test-sort test-master

test-mapper:
	@echo Testing mapper...
	@./test/mapper_test.py | sort > data/mapper_output_test.txt
	@diff --suppress-common-lines -y data/mapper_output_test.txt data/mapper_output.txt
	@rm data/mapper_output_test.txt

test-sort:
	@echo Testing sort...
	@./test/sort_test.py | tail -n 2 > data/sort_output_test.txt
	@diff --suppress-common-lines -y data/sort_output_test.txt data/sort_output.txt
	@rm data/sort_output_test.txt

test-master:
	@echo Testing master...
	@./test/master_test.py | sort > data/master_output_test.txt
	@diff --suppress-common-lines -y  data/master_output.txt
	@rm data/master_output_test.txt

bench:
	@echo Running sorting bench...
	@./test/run_bench.py