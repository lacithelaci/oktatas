from dataclasses import dataclass, field


@dataclass
class User:
    id: str = field(hash=True)
    name: str = field(repr=True, compare=False)
    age: int = field(repr=True, compare=False)
    country: str = field(repr=True, compare=False)

@dataclass
class Playlist:
    id: str = field(hash=True)
    owner_id: str = field(repr=True, compare=False)
    name: str = field(repr=True, compare=False)
    songs: int = field(repr=True, compare=False)
    private: bool = field(repr=True, compare=False, default=True)

@dataclass
class Song:
    id: str = field(hash=True)
    playlist_id: str = field(repr=True, compare=False)
    title: str = field(repr=True, compare=False)
    artist: str = field(repr=True, compare=False)
    genre: str = field(repr=True, compare=False)
