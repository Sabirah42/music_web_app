# POST albums Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Albums message route
POST /albums
  title: string
  release_year: int
  artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /albums
#  Parameters:
#    title: Voyage
#    release_year: 2022
#    artist_id: 2
#  Expected response (200 OK):
"""
None
"""

# GET /albums
#  Expected response (200 OK):
"""
Returns list of albums (Boxer, Voyage)
"""
```

## 3. Test-drive the Route

```python
"""
POST /albums
 Parameters:
   title: Boxer
   release_year: 2007
   artist_id: 1
 Expected response (200 OK):
"""
def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

"""
GET /albums
  Expected response (200 OK):
  Returns list of albums (Boxer, Brothers)
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == [
        Album(1,'Boxer', '2007', 1),
        Album(2, 'Voyage', '2022', 2)
        ]

```
