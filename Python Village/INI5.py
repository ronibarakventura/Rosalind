import os

file_path = os.path.expanduser("~/Desktop/rosalind_ini5.txt")

def dataset(file):
	open_file = open(file, "r")
	all_lines = open_file.readlines()
	my_lines = []
	for line in range(len(all_lines)):
		if line % 2 == 1:
			my_lines.append(all_lines[line])
	
	my_joined_lines = ""
	for line in my_lines:
		my_joined_lines += line
	
	print my_joined_lines
	open_file.close()