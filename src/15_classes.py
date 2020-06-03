# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    lat = 0.0
    lon = 0.0
    def __init__(self, lati, longi):
        self.lat = lati
        self.lon = longi

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    name = ""
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return self.name+', '+str(self.lon)+', '+str(self.lat)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return '\n'+self.name+': Difficulty Level – '+str(self.difficulty)+',\nSize – '+str(self.size)+', Lat – '+str(self.lon)+', Lon – '+str(self.lat)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

way1 = Waypoint('Catacombs',41.70505,-121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(way1)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

Newberry = Geocache("Newberry Views",1.5,2,44.05,-121.4)


# Print it--also make this print more nicely
print(Newberry)
