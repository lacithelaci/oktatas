class User:
    id: str
    name: str
    age: int
    country: str

    def __init__(self, id: str, name: str, age: int, country: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.country = country

    def __eq__(self, o: object) -> bool:
        return isinstance(o, User) and self.id == o.id

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "#{0}: {1} ({2}, {3})".format(self.id, self.name, self.age, self.country)

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, User):
            return NotImplemented

        return self.id < o.id


class Playlist:
    id: str
    owner_id: str
    name: str
    songs: int
    private: bool

    def __init__(self, id: str, owner_id: str, name: str, songs: int, private: bool) -> None:
        self.id = id
        self.owner_id = owner_id
        self.name = name
        self.songs = songs
        self.private = private

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Playlist) and self.id == o.id

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "#{0}: {1} ({2}) - {3}".format(self.id, self.name, self.songs, self.private)

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Playlist):
            return NotImplemented

        return self.id < o.id


class Song:
    id: str
    playlist_id: str
    title: str
    artist: str
    genre: str

    def __init__(self, id: str, playlist_id: str, title: str, artist: str, genre: str) -> None:
        self.id = id
        self.playlist_id = playlist_id
        self.title = title
        self.artist = artist
        self.genre = genre

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Song) and self.id == o.id

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "#{0}: {1} ({2}) - {3}".format(self.id, self.title, self.artist, self.genre)

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Song):
            return NotImplemented

        return self.id < o.id
