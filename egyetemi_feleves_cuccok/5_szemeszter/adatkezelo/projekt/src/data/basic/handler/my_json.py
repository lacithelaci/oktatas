import json
import os
from src.data.basic.model_dataclasses import User, Playlist, Song


def write_users_json(users: list[User], path: str) -> None:
    with open(os.path.join(path, "users.json"), "w") as file:
        json.dump([user.__dict__ for user in users], file)


def read_users_json(path: str, file_name: str = "users", extension: str = ".json") -> list[User]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            User(user["id"], user["name"],
                user["age"], user["country"])
            for user in json.load(file)
        ]
        """
        return json.load(file, object_hook=lambda d: User(**d))


def write_playlists_json(playlists: list[Playlist], path: str) -> None:
    with open(os.path.join(path, "playlists.json"), "w") as file:
        json.dump([playlist.__dict__ for playlist in playlists], file)


def read_playlists_json(path: str, file_name: str = "playlists", extension: str = ".json") -> list[Playlist]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            Playlist(playlist["id"], playlist["owner_id"],
            playlist["name"], playlist["songs"], playlist["private"])
            for playlist in json.load(file)
        ]
        """

        return json.load(file, object_hook=lambda d: Playlist(**d))


def write_songs_json(songs: list[Song], path: str) -> None:
    with open(os.path.join(path, "songs.json"), "w") as file:
        json.dump([song.__dict__ for song in songs], file)


def read_songs_json(path: str, file_name: str = "songs", extension: str = ".json") -> list[Song]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            Song(song["id"], song["playlist_id"],
            song["title"], song["artist"], song["genre"])
            for song in json.load(file)
        ]
        """

        return json.load(file, object_hook=lambda d: Song(**d))
