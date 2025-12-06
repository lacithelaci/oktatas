import os
import csv
from src.data.basic.model_dataclasses import User, Playlist, Song


def write_users_csv(users: list[User], path: str, file_name: str = "users.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "users.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "name", "age", "country"])
        for user in users:
            writer.writerow([user.id, user.name, user.age, user.country])


def read_users_csv(path: str, file_name: str = "users.csv", delimiter: str = ";"):
    with open(os.path.join(path, file_name if file_name is not None else "users.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        next(rows, None)
        users = [User(row[0], row[1], int(row[2]), row[3]) for row in rows]
        for user in users:
            print(f"   {user.id} {user.name} ({user.age}, {user.country})")


def write_playlists_csv(playlists: list[Playlist], path: str, file_name: str = "playlists.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "playlists.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "owner_id", "name", "songs", "private"])
        for playlist in playlists:
            writer.writerow([playlist.id, playlist.owner_id, playlist.name, playlist.songs, playlist.private])


def read_playlists_csv(path: str, file_name: str = "playlists.csv", delimiter: str = ";"):
    with open(os.path.join(path, file_name if file_name is not None else "playlists.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        next(rows, None)
        playlists = [Playlist(row[0], row[1], row[2], int(row[3]), row[4]) for row in rows]
        for playlist in playlists:
            print(f"   {playlist.id} {playlist.name} ({playlist.songs}, {playlist.private})")


def write_songs_csv(songs: list[Song], path: str, file_name: str = "songs.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "songs.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["id", "playlist_id", "title", "artist", "genre"])
        for song in songs:
            writer.writerow([song.id, song.playlist_id, song.title, song.artist, song.genre])


def read_songs_csv(path: str, file_name: str = "songs.csv", delimiter: str = ";"):
    with open(os.path.join(path, file_name if file_name is not None else "songs.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        next(rows, None)
        songs = [Song(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        for song in songs:
            print(f"   {song.id} {song.title} - {song.artist} ({song.genre})")
