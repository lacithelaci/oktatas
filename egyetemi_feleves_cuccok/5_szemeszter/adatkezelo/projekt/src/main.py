import random

import openpyxl
import pandas as pd

from src.data.basic.generator import generate_users, generate_playlists, generate_songs
from src.data.basic.handler.csv_list import write_users_csv, read_users_csv, write_playlists_csv,\
    read_playlists_csv, write_songs_csv, read_songs_csv
from src.data.basic.handler.my_json import write_users_json, read_songs_json, read_users_json, write_songs_json, \
    write_playlists_json, read_playlists_json
from src.data.basic.handler.sql import write_database, read_database, query
from src.data.basic.handler.xslx import read_users_xlsx, read_playlists_xlsx, read_songs_xlsx


def main():

    n = 10
    start = "\n\033[95m\033[1m• "
    end = "\033[0m"
    path = r"C:\Users\czliz\OneDrive\Dokumentumok\projekt"


    #RANDOM USERS
    print(start, n, "Random Users:", end)
    users = generate_users(n)
    for i in range(n):
        print("  ", users[i])

    user_ids = []
    for i in range(n):
        user_ids.append(users[i].id)

    u_ids = random.choices(user_ids, k=n)


    # RANDOM PLAYLISTS
    print(start, n, "Random Playlists:", end)
    playlists = generate_playlists(n, u_ids)
    for i in range(n):
        print("  ", playlists[i])

    playlist_ids = []
    for i in range(n):
        playlist_ids.append(playlists[i].id)

    p_ids = random.choices(playlist_ids, k=n)


    # RANDOM SONGS
    print(start, n, "Random Songs:", end)
    songs = generate_songs(n, p_ids)
    for i in range(n):
        print("  ", songs[i])


    # CSV - USERS
    try:
        write_users_csv(users, path)
    finally:
        print(start, n, "Users Successfully Written into CSV File!", end)
        print(start, "Data of 'users.csv' File:", end)

    read_users_csv(path)


    #CSV - PLAYLISTS
    try:
        write_playlists_csv(playlists, path)
    finally:
        print(start, n, "Playlists Successfully Written into CSV File!", end)
        print(start, "Data of 'playlists.csv' File:", end)

    read_playlists_csv(path)


    # CSV - SONGS
    try:
        write_songs_csv(songs, path)
    finally:
        print(start, n, "Songs Successfully Written into CSV File!", end)
        print(start, "Data of 'songs.csv' File:", end)

    read_songs_csv(path)


    #JSON - USERS
    try:
        write_users_json(users, path)
    finally:
        print(start, n, "Users Successfully Written into JSON File!", end)
        print(start, "Data of 'users.json' File:", end)

    for i in range(n):
        print("  ", read_users_json(path)[i])


    # JSON - PLAYLISTS
    try:
        write_playlists_json(playlists, path)
    finally:
        print(start, n, "Playlists Successfully Written into JSON File!", end)
        print(start, "Data of 'playlists.json' File:", end)

    for i in range(n):
        print("  ", read_playlists_json(path)[i])


    #JSON - SONGS
    try:
        write_songs_json(songs, path)
    finally:
        print(start, n, "Songs Successfully Written into JSON File!", end)
        print(start, "Data of 'songs.json' File:", end)

    for i in range(n):
        print("  ", read_songs_json(path)[i])


    #XLSX
    try:
        with pd.ExcelWriter(path + r"/data.xlsx", engine="openpyxl", mode="w") as writer:
            df = pd.DataFrame.from_records([u.__dict__ for u in users])
            df.to_excel(writer, sheet_name="users", index=False)
            df = pd.DataFrame.from_records([p.__dict__ for p in playlists])
            df.to_excel(writer, sheet_name="playlists", index=False)
            df = pd.DataFrame.from_records([s.__dict__ for s in songs])
            df.to_excel(writer, sheet_name="songs", index=False)
    finally:
        print(start, n, "Data Successfully Written into XLSX File!", end)
        print(start, "Data of 'data.xlsx' File:", end)

    start2 = "   \033[4m\033[36m"
    end2 = "\033[0m"


    w = openpyxl.load_workbook(path + r"/data.xlsx")
    print(start2 + "Sheet: users" + end2)
    for user in read_users_xlsx(w):
        print("  ", user)
    print(start2 + "Sheet: playlists" + end2)
    for playlist in read_playlists_xlsx(w):
        print("  ", playlist)
    print(start2 + "Sheet: songs" + end2)
    for song in read_songs_xlsx(w):
         print("  ", song)


    #ORACLE
    try:
        write_database(path + "/database.db", users, playlists, songs)
    finally:
        print(start, "Data Successfully Written into Database!", end)

    print(start, "Data of 'database.db' File:", end)
    read_database(path)

    print(start, "Playlists with More Than 400 Songs In it:", end)
    ps = query(path)
    for p in ps:
        print("  ", p)


if __name__ == '__main__':
    main()
