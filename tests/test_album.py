from lib.album import Album

"""
Constructs with id, title, release_date and artst_id
"""

def test_constructs():
    album = Album(1, "Boxer", 2007, 1)

    assert album.id == 1
    assert album.title == "Boxer"
    assert album.release_year == 2007
    assert album.artist_id == 1

"""
Albums with equal conttents are equal
"""

def test_equalises():
    album_1 = Album(1, "Title", 2000, 1)
    album_2 = Album(1, "Title", 2000, 1)

    assert album_1 == album_2

"""
Albums are returned as strings
"""
album = Album(1, "Title", 2000, 1)
assert str(album) == "Album(1, Title, 2000, 1)"