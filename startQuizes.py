import os
from subprocess import Popen,PIPE,check_output


# process = Popen(['python', 'pointers.py'],stdout=PIPE)
# for line in process.stdout:
#   print(line)

def print_menu(files):
	directory = []
	print "\nThe current Quizes to Run:"
	count = 0
	for file in files:
		size = len(file)
		#and file[size -2:size] == 'py' 
		if(file[0] != '.' and file != 'startQuizes.py' and (file[size -2:size] == 'py' or file[size -2:size] == 'ut')):
			print("\t%d)%s"%(count,file))
			directory.append(file)
			#__import__(file)
			count += 1
	print("\tEnter number, -1 to exit")
	return directory

def run_Program(choice,directory):
	quiz = directory[choice]
	size = len(quiz)

	if(quiz[size -2:size] == 'py'):
		execfile(os.path.realpath(quiz))
	elif(quiz[size -2:size] == 'ut'):
		process = Popen(os.path.realpath(quiz),stdin = PIPE)
		
		while(process.poll() == None):
			process.communicate(input())


if __name__ == "__main__":
	path = os.getcwd()
	files = os.listdir(path)

	#this is safe becuase I am not using user input to run shell commands
	Popen([os.path.realpath('make'),'make'],shell=True)

	yes =''
	no = ''

	more = True
	while(more):
		
		try:
			directory = print_menu(files)
			choice = input("\nWhat subject do you want to go over?(Enter number):")
			choice = int(choice)
			if(choice == -1):
				break
			elif( choice >= 0 and choice < len(directory)):
				yes = run_Program(choice,directory)
		except Exception as e:
			print e
			print "Not a valid input"
		# except NameError as n:
		# 	print "Not valid input\n\n"
		# except SyntaxError as s:
		# 	print "Not valid input\n\n"
		

