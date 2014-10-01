import os
from subprocess import Popen,PIPE


# process = Popen(['python', 'pointers.py'],stdout=PIPE)
# for line in process.stdout:
#   print(line)

def print_menu(files):
	directory = []
	print "\nThe current Quizes to Run:"
	count = 0
	for file in files:
		size = len(file)
		if(file[0] != '.' and file[size -2:size] == 'py' and file != 'startQuizes.py'):
			print("\t%d)%s"%(count,file))
			directory.append(file)
			count += 1
	print("\tEnter number, -1 to exit")
	return directory

def run_Program(choice,directory,type):
	pass



if __name__ == "__main__":
	path = os.getcwd()
	files = os.listdir(path)

	directory = print_menu(files)


	more = True
	while(more):
		
		try:
			choice = input("\nWhat subject do you want to go over?(Enter number):")
			choice = int(choice)
			if(choice == -1):
				break
			elif( choice >= 0 and choice < len(directory)):
				print "run the programs here"
		except Exception as e:
			print "Not a valid input"
		# except NameError as n:
		# 	print "Not valid input\n\n"
		# except SyntaxError as s:
		# 	print "Not valid input\n\n"
		

