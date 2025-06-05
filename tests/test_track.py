import pytest
from lib.track import *


def test_one_track_is_added():
    Spotify = tracker()
    Spotify.add_track("Despacito")
    assert Spotify.history() == ["Despacito"]
