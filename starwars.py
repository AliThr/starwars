import sys
from directory import *

if len(sys.argv) == 1:
    print Help().assist()
elif len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print Help().assist()
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
'''
elif len(sys.argv) == 4:
    if sys.argv[1] == "list":
        if sys.argv[2] == "-orderby":
            if sys.argv[3] == "mass":
                print SolarHelper().getPlanetsSortedByMass()
            elif sys.argv[3] == "diameter":
                print SolarHelper().getPlanetsSortedByDiameter()
            elif sys.argv[3] == "distance":
                print SolarHelper().getPlanetsInOrder()
            else:
                print Help().assist()
        elif sys.argv[2] == "-filterby":
            if sys.argv[3] ==  "mass":
                print SolarHelper().getPlanetsUnderACertainMass()
            elif sys.argv[3] ==  "diameter":
                print SolarHelper().getPlanetsOverACertainDiameter()
            else:
                print Help().assist()

        else:
            print Help().assist() 
    else:
        print Help().assist()
else:
    print Help().assist()
'''