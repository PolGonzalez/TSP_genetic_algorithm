import geopy as geo
from geopy.geocoders import Nominatim
from geopy import distance


class Instance:
    def __init__(self, n=None, cities=None):
        self.n = n
        self.cities = cities

        if self.n is None:
            self.generate_example_instance()

        assert self.n == len(self.cities)

        self.geolocator = Nominatim(user_agent="TSP")
        self.locations = [self.geolocator.geocode(city) for city in self.cities]

        # generate matrix of distances between cities (cost of each edge on our complete graph)
        self.dist = [
            [distance.distance((i.latitude, i.longitude), (j.latitude, j.longitude)).km for i in self.locations] for j
            in self.locations]

    def generate_example_instance(self):
        self.n = 15
        self.cities = ["barcelona", "paris", "tokyo", "new york", "delhi", "singapore",
                       "adelaide", "buenos aires", "dakar", "helsinki", "kabul", "lima", "miami", "vancouver",
                       "guayaquil"]

    def __str__(self):
        return "Instance with {} cities: {}".format(self.n, self.cities)
