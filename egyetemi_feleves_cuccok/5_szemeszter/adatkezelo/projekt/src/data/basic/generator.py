import random
from random import choice

from faker import Faker
from faker_music import MusicProvider
from src.data.basic.model_dataclasses import User, Playlist, Song


def generate_users(n: int, male_ratio: float = 0.5, locale: str = "en_US",
                    unique: bool = False, min_age: int = 15, max_age: int = 75) -> list[User]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    fake = Faker(locale)

    r = []
    while len(r) < 15:
        num = random.randint(1, 100)
        if num not in r:
            r.append(num)

    azon = (random.sample(r, n))

    users = []
    for i in range(n):
        male = random.random() < male_ratio
        generator = fake if not unique else fake.unique
        users.append(User(
            "U-" + str(azon[i]),
            generator.name_male() if male else generator.name_female(),
            random.randint(min_age, max_age),
            generator.country()))

    return users


def generate_playlists(n: int, u_ids: list[str], private_ratio: float = 0.5, locale: str = "en_US",
                  min_songs: int = 1, max_songs: int = 700) -> list[Playlist]:
    assert n > 0
    assert 0 < private_ratio < 1

    fake = Faker(locale)

    r = []
    while len(r) < 15:
        num = random.randint(300, 400)
        if num not in r:
            r.append(num)

    azon = (random.sample(r, n))

    playlists = []
    for i in range(n):
        title = fake.sentence()
        title = title.split()[0:2]
        private = random.random() < private_ratio
        playlists.append(Playlist(
            "P-" + str(azon[i]),
            str(choice(u_ids)),
            f"{title[0]} {title[1]}",
            random.randint(min_songs, max_songs),
            private))

    return playlists


def generate_songs(n: int, p_ids: list[str], attempts: int = None) -> list[Song]:
    assert n > 0
    assert attempts is None or attempts >= n

    fake = Faker()
    fake.add_provider(MusicProvider)

    r = []
    while len(r) < 15:
        num = random.randint(600, 800)
        if num not in r:
            r.append(num)

    azon = (random.sample(r, n))

    songs = []
    for i in range(n):
        title = fake.sentence()
        title = title.split()[0:2]
        songs.append(Song(
            "S-" + str(azon[i]),
            str(choice(p_ids)),
            f"{title[0]} {title[1]}",
            fake.first_name() + " " + fake.last_name(),
            fake.music_genre()))

    return songs
