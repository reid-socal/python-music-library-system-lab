#!/usr/bin/env python3


class Song:
    """A song, plus class-level statistics about every Song created."""

    # Class attributes: shared by every Song instance
    count = 0            # total number of songs created
    genres = []          # unique genres of all songs
    artists = []         # unique artists of all songs
    genre_count = {}     # e.g. {"Rap": 5, "Rock": 1}
    artist_count = {}    # e.g. {"Beyonce": 17, "Jay-Z": 40}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every new song updates the class-level statistics
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list if it is not already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list if not already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the genre's count, starting at 1 for a new genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the artist's count, starting at 1 for a new artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1