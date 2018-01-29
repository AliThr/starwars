import urllib3
urllib3.disable_warnings()
http = urllib3.PoolManager()
from urllib3.contrib import pyopenssl
pyopenssl.inject_into_urllib3()
import ast


class Help():
    """This class contains the 'assist' function that is shown whenever an incorrect function is placed in the command line."""
    def __init__(self):
        pass
    
    def assist(self):
        return """\n
     _______.___________.    ___      .______     ____    __    ____  ___      .______          _______.   .______   ____    ____ 
    /       |           |   /   \     |   _  \    \   \  /  \  /   / /   \     |   _  \        /       |   |   _  \  \   \  /   / 
   |   (----`---|  |----`  /  ^  \    |  |_)  |    \   \/    \/   / /  ^  \    |  |_)  |      |   (----`   |  |_)  |  \   \/   /  
    \   \       |  |      /  /_\  \   |      /      \            / /  /_\  \   |      /        \   \       |   ___/    \_    _/   
.----)   |      |  |     /  _____  \  |  |\  \----.  \    /\    / /  _____  \  |  |\  \----.----)   |    __|  |          |  |     
|_______/       |__|    /__/     \__\ | _| `._____|   \__/  \__/ /__/     \__\ | _| `._____|_______/    (__) _|          |__|     
                                                                                                                                  
To print details and an interesting fact about individual planets: starwars.py planet <planet number>
Planet Numbers:
---
1: Tatooine

2: Alderaan

3: Yavin IV

4: Hoth

5: Dagobah

6: Bespin

7: Endor

8: Naboo

9: Coruscant

10: Kamino

11: Geonosis"""


class APIGrabber():
    def __init__(self):
        pass

    def pullDataFromAPI(self, planetChoice):
        url = "https://swapi.co/api/planets/" + str(planetChoice) + "/" + "?format=json"
        APIData = http.request('GET', url)
        planetData = ast.literal_eval(APIData.data)
        return planetData

    def getPlanetName(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetName = planetData["name"]
        return planetName

    def getPlanetRotationalPeriod(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetRotationalPeriod = planetData["rotation_period"]
        return planetRotationalPeriod

    def getPlanetOrbitalPeriod(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetOrbitalPeriod = planetData["orbital_period"]
        return planetOrbitalPeriod

    def getPlanetDiameter(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetDiameter = planetData["diameter"]
        return planetDiameter

    def getPlanetClimate(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetClimate = planetData["climate"]
        return planetClimate

    def getPlanetGravity(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetGravity = planetData["gravity"]
        return planetGravity

    def getPlanetTerrain(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetTerrain = planetData["terrain"]
        return planetTerrain

    def getPlanetSurfaceWaterPercentage(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetSurfaceWater = planetData["surface_water"]
        return planetSurfaceWater

    def getPlanetPopulation(self, planetChoice):
        planetData = self.pullDataFromAPI(planetChoice)
        planetPopulation = planetData["population"]
        return planetPopulation

    def returnPlanetInformation(self, planetChoice):
        print "Planet name: " + self.getPlanetName(planetChoice)
        print "Planet rotational period: " + self.getPlanetRotationalPeriod(planetChoice)
        print "Planet orbital period: " + self.getPlanetOrbitalPeriod(planetChoice)
        print "Planet diameter: " + self.getPlanetDiameter(planetChoice)
        print "Planet climate: " + self.getPlanetClimate(planetChoice)
        print "Planet gravity: " + self.getPlanetGravity(planetChoice)
        print "Planet terrain: " + self.getPlanetTerrain(planetChoice)
        print "Planet percentage surface water: " + self.getPlanetSurfaceWaterPercentage(planetChoice)
        print "Planet population: " + self.getPlanetPopulation(planetChoice)

    