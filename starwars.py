import sys
from directory import *

if len(sys.argv) == 1:
    print Help().assist()
elif len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print Help().assist()
    elif sys.argv[1] == "--version":
        print Help().version()
    else:
        print Help().assist()
elif len(sys.argv) == 3:
    if sys.argv[1] == "planet":
        planetChoice = sys.argv[2]
        if int(sys.argv[2]) <= 61 and int(sys.argv[2]) > 0:
            APIGrabber().returnPlanetInformation(planetChoice)
        else:
            print "There are only 61 available planets. Please choose again."
    else:
        print Help().assist()
else:
    print Help().assist()


