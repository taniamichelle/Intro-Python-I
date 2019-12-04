# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
#parent class
class LatLon:
    #constructor
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    #get lat
    def get_lat(self):
        return self.lat
    #get lon
    def get_lon(self):
        return self.lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
#child class
class Waypoint(LatLon):
    #constructor
    def__init__(name, lat, lon):
        super().__init__(name, lat, lon)
        self.name = name
        #invoke __init__ of parent class
        LatLon.__init__(self, lat, lon)
    #get name
    def get_name(self):
        return self.name
        
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
#grandchild class
class Geocache(Waypoint):
    def__init__(name, lat, lon, difficulty, size):
        super().__init__(name, lat, lon, difficulty, size)
        self.difficulty = difficulty
        self.size = size
    #get size
    def get_size(self):
        return self.size
    #get difficulty
    def get_difficulty(self):
        return self.difficulty

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
w = Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
print(w.__str__())
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
g = Geocache("Newberry Views", 44.052137, -121.41556, 1.5, 2)
# Print it--also make this print more nicely
print(geocache)
print(g.__str__())