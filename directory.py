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

    def version(self):
        return "1.0"
    
    def assist(self):
        return """\n

  ___  ____   __    ____  _    _    __    ____  ___    ____  _  _ 
 / __)(_  _) /__\  (  _ \( \/\/ )  /__\  (  _ \/ __)  (  _ \( \/ )
 \__ \  )(  /(__)\  )   / )    (  /(__)\  )   /\__ \   )___/ \  / 
 (___/ (__)(__)(__)(_)\_)(__/\__)(__)(__)(_)\_)(___/()(__)   (__)    
                                                                                                                                  
To print details and an interesting fact about individual planets: starwars.py planet <planet number>
Planet Numbers:
---
1: Tatooine         2: Alderaan         3: Yavin IV         

4: Hoth             5: Dagobah          6: Bespin

7: Endor            8: Naboo            9: Coruscant        

10: Kamino          11: Geonosis        12. Utapu

13. Mustafar        14. Kashyyyk        15. Polis Massa     

16. Mygeeto         17. Felucia         18. Cato Neimoidia

19. Saleucami       20. Stewjon         21. Eriadu          

22. Corellia        23. Rodia           24. Nal Hutta

25. Dantooine       26. Bestine         27. Ord Mantell     

28. Unknown         29. Trandosha       30. Socorro

31. Mon Cala        32. Chandrila       33. Sullust         

34. Toydaria        35. Malastare       36. Dathomir

37. Ryloth          38. Aleen Minor     39. Vulpter         

40. Troiken         41. Tund            42. Haruun Kal

43. Cerea           44. Glee Anselm     45. Iridonia       

46. Tholoth         47. Iktotch         48. Quermia

49. Dorin           50. Champala        51. Mirial          

52. Serenno         53. Concord Dawn    54. Zolan

55. Ojom            56. Skako           57. Muunilinst      

58. Shili           59. Kalee           60. Umbara

                    61. Jakku"""

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
