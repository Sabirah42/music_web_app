from lib.album import Album
# from lib.album_repository import AlbumRepository

# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)" 

# === End Example Code ===

"""
POST /albums
Parameters:
title: Boxer
release_year: 2007
artist_id: 1
Expected response (200 OK):
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    post_response = web_client.post('/albums', data={
        'title': 'Voyage', 
        'release_year': '2022', 
        'artist_id': '2'
        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == [
    "Album(1, 'Boxer', 2007, 1)",
    "Album(2, 'Voyage', 2022, 2)"
    ]



"""
GET /albums
Expected response (200 OK):
Returns list of albums (Boxer, Brothers)
"""
# def test_get_albums(web_client):
#     response = web_client.get('/albums')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == [
#         Album(1,'Boxer', '2007', 1),
#         Album(2, 'Voyage', '2022', 2)
#         ]


