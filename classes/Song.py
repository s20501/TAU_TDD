class Song:
    def __init__(self, song_path):
        song = []

        with open(song_path, 'r') as f:
            for line in f:
                if line != '\n':
                    song.append(line)
        self.song = song

    def get_verse(self, n):
        if n < 1 or n > len(self.song):
            raise ValueError("Invalid verse number")
        else:
            return self.song[n - 1]

    def get_verse_range(self, start, end):
        song_len = len(self.song)
        if start < 1 or start > song_len or end > song_len or start > end:
            raise ValueError("Invalid verse number")

        result = []

        for i in range(start, end + 1):
            result.append(self.get_verse(i))

        return result

    def get_full_song(self):
        return self.song
