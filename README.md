AutomatedReview
===============

Program that makes it easy to add sections to a review that consists of quiz type information
from the command line

Reads files in current directory and lists files with .py or .out extension.
.out files are generated based on what the user puts in the make file.
'make' command is run before it reads the directory so it can include the .out files.

Not extensively tested at the moment.
The startQuizes.py file is the main file which runs everything catches and prints out all exceptions including those
that are recieved from subprocesses.
