from __future__ import division #this is for floating point division

def instantiation_correct1(label):
	print label + " i = 2"
	print label + "* j = &i"
	#if you make the input something other than a python defined value
	#you must create a variable of the input
	true = True 
	false = False 
	answer = input('This correctly assign a pointer?(true or false):')

	if(answer):
		print 'Correct!'
		return 1
	print "Incorrect, this is the correct way to assign a pointer"
	return 0

def value_question():
	yes = False
	no = True
	print '\nassert(*j == 2)'
	answer = input('Will this assertion fail?(yes or no):')

	if(answer):
		print 'Correct!'
		return 1
	print 'Incorrect dereferencing a correctly assigned pointer gives you the value it is pointing at'
	return 0

if __name__ == "__main__":
	total = 2
	correct = 0
	correct += instantiation_correct1('int')
	correct += value_question()

	print 'You got ' + str(correct/total * 100) + "% correct"
