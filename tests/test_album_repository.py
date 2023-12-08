from lib.album_repository import AlbumRepository
from lib.album import Album

def test_returns_all_albums(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repository = AlbumRepository(db_connection)

    assert repository.all() == [Album(1,'Boxer', 2007, 1)]

def test_creates_album(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Alligator', 2005, 1)
    repository.create(album)

    assert repository.all() == [
        Album(1,'Boxer', 2007, 1),
        Album(2,'Alligator', 2005, 1)
    ]