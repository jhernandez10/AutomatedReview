from __future__ import division #this is for floating point division

yes = False
no = True

def instantiation_correct1(label):
	print label + " i = 2"
	print label + "* j = &i"
	#if you make the input something other than a python defined value
	#you must create a variable of the input
	true = True 
	false = False 
	answer = input('This correctly assign a pointer?(true or false):')

	if(answer):
		print 'Correct!\n'
		return 1
	print "Incorrect, this is the correct way to assign a pointer\n"
	return 0

def value_question():
	yes = True
	no = False
	print "int i = 2"
	print "int* j = &i"
	print 'assert(*j == 2)'
	answer = input('Will this assertion fail?(yes or no):')

	if(answer):
		print 'Correct!\n'
		return 1
	print 'Incorrect dereferencing a correctly assigned pointer gives you the value it is pointing at\n'
	return 0

def value_question2():
	yes = True
	no = False
	print "int i = 2"
	print "int* j = &i"
	print "++*j"
	print 'assert(*j == 2)'

	answer = input('Will this assertion fail?(yes or no):')

	if(not answer):
		print 'Correct!\n'
		return 1
	print "Incorrect dereferencing a pointer allows you to modify it' value\n"
	return 0

def value_question3():
	yes = True
	no = False
	print "int i = 2"
	print "int* j = &i"
	print "++j"
	print 'assert(*j == 2)'

	answer = input('Will this assertion fail?(yes or no):')

	if(answer):
		print 'Correct!\n'
		return 1
	print( "Incorrect. Without first dereferencing a pointer the ++ operator moves a pointer forward.\n" +
			"In an array this makes sense but when assigned to a single value it moves the pointer to the next\n" +
			"position which contains an entirely unknow value.\n" )
	return 0

def reference_question1():
	yes = True
	no = False
	print 'int k = 2'
	print 'int&r = k'
	answer =  input('Is this the correct way to assign a reference?(yes or no):')

	if(answer):
		print 'Correct!\n'
		return 1
	print "Incorrect. In order to assign a reference you must give it an address to point to this way\n"
	return 0

def reference_question2():
	yes = True
	no = False
	print 'int k = 2'
	print 'int&r;'
	print 'r = &k'
	answer =  input('Is this the correct way to assign a reference?(yes or no):')

	if(not answer):
		print 'Correct!\n'
		return 1
	print "Incorrect you must assign a reference immediately\n"
	return 0

def reference_question3():
	yes = True
	no = False
	print 'int k = 2'
	print 'int&r = k'
	print 'assert(r == 3)'
	answer =  input('Does this assertion fail?(yes or no):')

	if(answer):
		print 'Correct!\n'
		return 1
	print "Incorrect. A reference is indistinguishable from the variable it references\n"
	return 0 

def reference_question4():
	yes = True
	no = False
	print 'int   i = 2'
	print 'int*  p = &i'
	print 'int*& r = p'
    
	answer = input('Does this reference work?(yes or no):')

	if(answer):
		print 'Correct!\n'
		return 1
	print 'Incorrect. The final line creates a reference to a pointer which is legal\n'
	return 0

def reference_question5():
	yes = True
	no = False
	print 'int   i = 2'
	print 'int*  p = &i'
	print 'int*& r = p'
	print '++*r'
	print 'assert(i  == 3)'
    
	answer = input('Does this assertion fail?(yes or no):')

	if(not answer):
		print 'Correct!\n'
		return 1
	print 'Incorrect. Since r is a reference to a pointer it is legal to dereference it and increment\n'
	return 0

if __name__ == "__main__":
	total = 8
	correct = 0
	correct += instantiation_correct1('int')
	correct += value_question()
	correct += value_question2()
	correct += value_question3()
	correct += reference_question1()
	correct += reference_question2()
	correct += reference_question3()
	correct += reference_question4()
	correct += reference_question5()


	print 'You got ' + str(correct/total * 100) + "% correct"
