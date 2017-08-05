#!/usr/bin/python
import sys
def modify(func, s):
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2], 'w')#creates a new text file

    for x in input:
        l = x.split(' ')
        num = int(l[1])
        r = func
        result = r(num)
        if((l[0] == 'walkLunge') | (l[0] == 'stepUp')):
            if(result%2 != 0):
                result = result + 1
        if(l[0] not in s):
            output.write('%s %s\n' % (l[0], result))
        else:
            output.write('%s %s\n' % (l[0], int(num * .5)))
            
    print "You have a new workout written to " + sys.argv[2] 
    input.close()
    output.close()

#put the arg list in a hash table
s = set() 
for x in sys.argv:
    s.add(x)

choice = True
while choice:
    print '''
I increase intensity (except fails)
m maintain intensity (except fails)
r reduce intensity 
i instructions
q quit'''
    user = raw_input('Enter a command: ')

    if(user == 'i'):
        print '''In the command line arguments enter the incoming 
workout, followed by the name of the file for your new 
workout, followed by a list of the exercises from 
your previous workout that you were unable to complete
the prescribed number of repetions.
For example,
user/file$./workout.py input.txt output.txt rfess cGPU

Then select how you wish to progress.  This workout is 
designed for athletes who have experience performing 
the exercises but who have not performed calithensics for
a signifcant period of time.  Progression is expected
to be moderate or aggressive.  Inexperienced athletes or
athletes who are within a late stage training status
should seek a more approrpiate workout.

Athletes who are having difficulty increasing repetitions
should select 'm' (maintain training intensity).  Athletes who are 
experiencing overtraining symptoms such as soreness or
excessive fatigue should select 'r' (reduce training intensity).  
Athletes who have waited more than a week since there 
previous workout should also select 'r'.
Otherwise the athlete should select capital 'I' 
to increase intesity.

This workout should be performed two to three days 
per week on non-consecutive days with approximately
even rest periods in between each workout.'''
    elif (len(sys.argv) < 3):
        print 'You did not enter enough arguments.'
    elif (user == 'I'):
        f = lambda x: x + 1 if (x < 10) else x + int(x * .1) 
        modify(f, s)
        choice = False
    elif (user == 'm'):
        f = lambda x: x
        modify(f, s)
        choice = False
    elif (user == 'r'):
        f = lambda x: x if (x == 0) else int(x * .5)
        modify(f, s)
        choice = False
    elif (user == 'q'):
        choice = False
    else:
        print 'Invalid Argument'
