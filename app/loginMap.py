#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import GoogleV3

geolocator = GoogleV3()

cities = ['Amsterdam', 'Milan', 'Dallas', 'Los Angeles', 'Montreal', 'Lenoir', 'Nottingham', 'Rotterdam', 'Dusseldorf',
          'Falkenstein', 'Roubaix', 'Tokyo', 'Sydney']
#cities = []


class myMap:
    def __init__(self, cities):
        self.cities = cities
    def generate_map(self):
        figure = plt.figure()
        plt.subplot(111)

        lat, lon = [], []

        # loop through the cities and save latitude and longitude
        for city in self.cities:
            address, (latitude, longitude) = geolocator.geocode(city)
            lat.append(latitude)
            lon.append(longitude)

        # generate map plot
        map = Basemap(projection='cyl', resolution='l')
        map.bluemarble()

        # map city coordinates to map coordinates
        x, y = map(lon, lat)

        # draw a red dot at cities coordinates
        plt.plot(x, y, 'ro', markersize=3)

        return figure.savefig('login.png')

newmap = myMap(cities)
newmap.generate_map()

