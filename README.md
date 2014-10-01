AutomatedReview
===============

Program that makes it easy to add sections to a review that consists of quiz type information
from the command line

Reads files in current directory and lists files with .py or .out extension.
if you don't run the make command before you run the program it doesn't include the .out files.
Not entirely sure why just yet but if you just run the program exit then run it again it includes them.

Not extensively tested at the moment.
The startQuizes.py file is the main file which runs everything catches and prints out all exceptions including those
that are recieved from subprocesses.
