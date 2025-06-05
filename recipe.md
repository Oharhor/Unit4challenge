# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
so that I can keep track of my music-listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

class Tracker():
    def __init__(self):
        self.tracklist = []
    def add_track(self, track = ""):
        self.tracklist.append('track')
    def history(self):
        return self.tracklist

1. Class is called "Tracker" because an object in it can use methods to track certain inputs (i.e. song titles).

2. Init method creates an empty list accessible to every method of the class.

3. User enters track which is then added to list in init.

4. List is returned with all values added using add_track so far - only return value.

## 3. Create Examples as Tests

""""
When one track is added via add_track 
self.history should return a list with one string
add_track("track") => self.history == ["track"]
"""

"""
When no track is added via add_track
self.history should return an empty list
self.history => [""]
"""

"""
When three tracks are added via add_track
self.history should return a list with 3 strings
self.history => ["track1", "track2", "track3"]

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

