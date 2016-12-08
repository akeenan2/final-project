test: test-mapper test-sort test-master

test-mapper:
	@echo Testing mapper...
	@./test/mapper_test.py | sort > data/mapper_output_test.txt
	@diff --suppress-common-lines -y data/mapper_output_test.txt data/mapper_output.txt
	@rm data/mapper_output_test.txt

test-sort:
	@echo Testing sort...
	@./test/sort_test.py
	@rm data/*_test.txt

test-master:
	@echo Testing master...
	@./test/master_test.py | sort > data/master_output_test.txt
	@diff --suppress-common-lines -y  data/master_output_test.txt data/master_output.txt
	@./test/master_test.py > data/master_output_test.txt
	@./test/check_sort.py -f data/master_output_test.txt
	@rm data/master_output_test.txt

bench:
	@./test/bench.py

key-words:
	@./src/master.py -t -d -n 11 > data/top-words.txt
	@./graph-scripts/top-words.py