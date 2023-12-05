from lib.album_repository import AlbumRepository
from lib.album import Album

def test_returns_all_albums(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repository = AlbumRepository(db_connection)

    assert repository.all() == [Album(1,'Boxer', 2007, 1)]