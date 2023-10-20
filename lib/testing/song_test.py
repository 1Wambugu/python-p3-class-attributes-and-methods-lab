from song import Song

class TestSong:
    '''Class "Song" in song.py'''

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_counts_total_number_of_Song_objects(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 1)  # Change the expected count to 1
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 2)  # Change the expected count to 2

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Jay-Z" in Song.artists)
        assert("Beyonce" in Song.artists)
        assert("Hall and Oates" in Song.artists)

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)  # Check that the "Rap" count is 1
        assert(Song.genre_count["Pop"] == 2)  # Check that the "Pop" count is 2
        assert(Song.genre_count["Rock"] == 1)  # Check that the "Rock" count is 1

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count["Jay-Z"] == 1)  # Check that the "Jay-Z" count is 1
        assert(Song.artist_count["Beyonce"] == 1)  # Check that the "Beyonce" count is 1
        assert(Song.artist_count["Nirvana"] == 0)  # Check that the "Nirvana" count is 0
        assert(Song.artist_count["Hall and Oates"] == 2)  # Check that the "Hall and Oates" count is 2

    def test_has_artists_after_adding_song(self):
        '''checks if artists are updated after adding a new song.'''
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        self.assertIn("Jay-Z", Song.artists)

    def test_has_genres_after_adding_song(self):
        '''checks if genres are updated after adding a new song.'''
        song2 = Song("Halo", "Beyonce", "Pop")
        self.assertIn("Pop", Song.genres)
        self.assertNotIn("Rock", Song.genres)

# Run the tests
if __name__ == '__main__':
    test = TestSong()
    test.test_saves_name_artist_genre()
    test.test_counts_total_number_of_Song_objects()
    test.test_has_genres()
    test.test_has_artists()
    test.test_has_genre_count()
    test.test_has_artist_count()
    test.test_has_artists_after_adding_song()
    test.test_has_genres_after_adding_song()
