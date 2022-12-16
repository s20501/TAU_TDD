import unittest

from classes.Song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('song.txt')

    def test_get_verse(self):
        verse = self.song.get_verse(1)
        self.assertEqual(verse, "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n")

    def test_get_verse_invalid(self):
        with self.assertRaises(ValueError):
            self.song.get_verse(0)

    def test_get_verse_range(self):
        verses = self.song.get_verse_range(1, 3)
        self.assertEqual(verses,
                         ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n",
                          "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n",
                          "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n"])

    def test_get_verse_range_invalid_start(self):
        with self.assertRaises(ValueError):
            self.song.get_verse_range(0, 3)

    def test_get_verse_range_invalid_end(self):
        with self.assertRaises(ValueError):
            self.song.get_verse_range(3, 1)

    def test_get_full_song_long(self):
        song = self.song.get_full_song()
        self.assertEqual(len(song), 12)

    def test_get_full_song_verse(self):
        song = self.song.get_full_song()
        self.assertEqual(song[1],
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n")


if __name__ == '__main__':
    unittest.main()
