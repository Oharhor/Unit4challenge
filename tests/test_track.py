import pytest
from lib.track import *


def test_one_track_is_added():
    Spotify = tracker()
    Spotify.add_track("Despacito")
    assert Spotify.history() == ["Despacito"]

def test_no_track_is_added():
    Soundcloud = tracker()
    Soundcloud.add_track()
    assert Soundcloud.history() == [""]

def test_three_tracks_are_added():
    AppleMusic = tracker()
    AppleMusic.add_track("song1")
    AppleMusic.add_track("song2")
    AppleMusic.add_track("song3")
    assert AppleMusic.history() == ["song1", "song2", "song3"]