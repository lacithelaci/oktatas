import sqlite3
from src.data.basic.model_dataclasses import User, Playlist, Song


def write_database(name: str, users: list[User], playlists: list[Playlist], songs: list[Song], create = True):

    #CREATE CONNECTION
    conn = sqlite3.connect(name)
    cursor = conn.cursor()


    #DELETE TABLES
    if create:
        cursor.execute(f"""
                        DROP TABLE USER
                        """)

        cursor.execute(f"""
                        DROP TABLE PLAYLIST
                        """)

        cursor.execute(f"""
                        DROP TABLE SONG
                        """)


    #CREATE TABLES
    cursor.execute(f"""
                    CREATE TABLE USER(
                    id TEXT primary key, 
                    name TEXT, 
                    age INTEGER, 
                    country TEXT)
                    """)

    cursor.execute(f"""
                    CREATE TABLE PLAYLIST(
                    id TEXT primary key, 
                    owner_id TEXT, 
                    name TEXT, 
                    songs INTEGER,
                    private INTEGER,
                    FOREIGN KEY (owner_id) REFERENCES USER(id))
                    """)

    cursor.execute(f"""
                    CREATE TABLE SONG(
                    id TEXT primary key, 
                    playlist_id TEXT, 
                    title TEXT, 
                    artist TEXT,
                    genre TEXT,
                    FOREIGN KEY (playlist_id) REFERENCES PLAYLIST(id))
                    """)


    #INSERT DATA
    cursor.executemany(f"""
                            INSERT INTO USER
                            (id, name, age, country)
                            VALUES(?, ?, ?, ?)
                            """,
                           [(user.id, user.name,
                             user.age, user.country)
                            for user in users])

    cursor.executemany(f"""
                            INSERT INTO PLAYLIST
                            (id, owner_id, name, songs, private)
                            VALUES(?, ?, ?, ?, ?)
                            """,
                           [(playlist.id, playlist.owner_id,
                             playlist.name, playlist.songs, playlist.private)
                            for playlist in playlists])

    cursor.executemany(f"""
                            INSERT INTO SONG
                            (id, playlist_id, title, artist, genre)
                            VALUES(?, ?, ?, ?, ?)
                            """,
                       [(song.id, song.playlist_id,
                        song.title, song.artist, song.genre)
                        for song in songs])


    #CLOSE CONNECTION
    conn.commit()
    cursor.close()
    conn.close()


def read_database(path: str):

    con = sqlite3.connect(path + "/database.db")
    cursor = con.cursor()

    #USER TABLE
    result = cursor.execute(f"""
                            SELECT id, name, age, country FROM USER
                            """)
    users = []
    u = result.fetchall()
    for user in u:
        users.append(User(user[0], user[1],
                             user[2], user[3]))


    #PLAYLIST TABLE
    result = cursor.execute(f"""
                            SELECT id, owner_id, name, songs, private FROM PLAYLIST
                            """)
    playlists = []
    p = result.fetchall()
    for playlist in p:
        private = playlist[4]
        if private == 0:
            private = False
        else:
            private = True
        playlists.append(Playlist(playlist[0], playlist[1],
                             playlist[2], playlist[3], private))


    #SONG TABLE
    result = cursor.execute(f"""
                            SELECT id, playlist_id, title, artist, genre FROM SONG
                            """)
    songs = []
    s = result.fetchall()
    for song in s:
        songs.append(Song(song[0], song[1],
                             song[2], song[3], song[4]))

    start2 = "   \033[4m\033[36m"
    end2 = "\033[0m"

    print(start2 + "Table: USER" + end2)
    for u in users:
        print("  ", u)

    print(start2 + "Table: PLAYLIST" + end2)
    for p in playlists:
        print("  ", p)

    print(start2 + "Table: SONG" + end2)
    for s in songs:
        print("  ", s)


def query(path):
    conn = sqlite3.connect(path + "/database.db")
    cursor = conn.cursor()

    query = f"""
            SELECT * FROM PLAYLIST
            WHERE songs > 400
            """

    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows
