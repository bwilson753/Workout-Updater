# Workout-Updater (Read this raw)
This is a program that updates a series or circuit of calisthenic exercises as the user's training status changes.  It 
was created using the python langauge and was designed to be run on a linux ubuntu operating system.  It needs to be initialized
by providing a workout written to a text file.  The workout should be written so that each line of the workout is written
as a single set of one exercise followed by a number of repetitions.  Each exercise name should be followed by a single space and each 
number of repetitions should be followed by a newline whenever it is followed by another exercise.  For example,
pusUp 10
squat 20
invRow 10
Note that there is no extra whitespace after the final exercise.  It is assumed the user will follow the proper formatting guidelines.
A sample workout (sample.txt) has been provided.  The new workout, the updated workout, and any exercises that could not be completed must
be provided in the arguments when running the file.  For example,
$./workout.py sample.txt update.txt invRow
Further instructions are available once the program has been run.
