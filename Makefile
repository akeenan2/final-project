test: setup test-mapper test-sort test-master

setup:
	gcc -c src/measure.cpp -o src/measure

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
	@./test/check_sort.py -f master_output_test.txt
	@rm data/master_output_test.txt

clean:
	rm src/measure data/*_test.txt

bench:
	@echo Running sorting bench...
	@./test/bench.py
