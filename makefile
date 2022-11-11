.PHONY : all
all : smurftown 

smurftown : smurftown.py computations.py parse_file.py Player.py
	python smurftown.py data_test_massive.txt

gen_data : generate_data.py
	python generate_data.py -b10 -n20000 -c2 data_test_massive.txt

.PHONY : clean
clean : 
	rm all_cycles_final.txt all_cycles_including_doublets.txt