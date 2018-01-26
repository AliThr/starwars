import urllib3
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

    def getPlanetName(self, planetData):
        planetName = planetData["name"]
        return planetName

    def getPlanetRotationalPeriod(self, planetData):
        planetRotationalPeriod = planetData["rotation_period"]
        return planetRotationalPeriod

    def getPlanetOrbitalPeriod(self, planetData):
        planetOrbitalPeriod = planetData["orbital_period"]
        return planetOrbitalPeriod

    def getPlanetDiameter(self, planetData):
        planetDiameter = planetData["diameter"]
        return planetDiameter

    def getPlanetClimate(self, planetData):
        planetClimate = planetData["climate"]
        return planetClimate

    def getPlanetGravity(self, planetData):
        planetGravity = planetData["gravity"]
        return planetGravity

    def getPlanetTerrain(self, planetData):
        planetTerrain = planetData["terrain"]
        return planetTerrain

    def getPlanetSurfaceWaterPercentage(self, planetData):
        planetSurfaceWater = planetData["surface_water"]
        return planetSurfaceWater

    def getPlanetPopulation(surface_water):
        planetPopulation = planetData["population"]
        return planetPopulation

    def returnPlanetInformation(self, planetChoice):
        print self.getPlanetName(planetData)
        print self.getPlanetRotationalPeriod(planetData)
        print self.getPlanetOrbitalPeriod(planetData)
        print self.getPlanetDiameter(planetData)
        print self.getPlanetClimate(planetData)
        print self.getPlanetGravity(planetData)
        print self.getPlanetTerrain(planetData)
        print self.getPlanetSurfaceWaterPercentage(planetData)
        print self.getPlanetPopulation(planetData)

    