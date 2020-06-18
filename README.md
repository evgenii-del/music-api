# API for music apps.
### How to use API?
Fields Track:
 - Album
 - Title
 - Description
 - Track
 - Image
 - Slug
 - Genre
 -  musician

Get all tracks:
**GET** `"http://khasanov.pythonanywhere.com/api/v1/tracks/"`

Create new track:
**POST** `"http://khasanov.pythonanywhere.com/api/v1/tracks/"`

Change track:
**PUT** `"http://khasanov.pythonanywhere.com/api/v1/tracks/<id>/"`

Delete track:
**DELETE** `"http://khasanov.pythonanywhere.com/api/v1/tracks/<id>/"`

Fields Album:
 - Title
 - Slug
 - Image
 - Description
 - musician

Get all albums:
**GET** `"http://khasanov.pythonanywhere.com/api/v1/albums/"`

Create new album:
**POST** `"http://khasanov.pythonanywhere.com/api/v1/albums/"`

Change album:
**PUT** `"http://khasanov.pythonanywhere.com/api/v1/albums/<id>/"`

Delete album:
**DELETE** `"http://khasanov.pythonanywhere.com/api/v1/albums/<id>/"`

Get all genres:
**GET** `"http://khasanov.pythonanywhere.com/api/v1/genres/"`

Register new user:
**POST** `http://khasanov.pythonanywhere.com/auth/users/`

Get info about user:
**GET** `http://khasanov.pythonanywhere.com/auth/users/me/`

Update user:
**PUT** `http://khasanov.pythonanywhere.com/auth/users/me/`

Login:
**POST** `http://khasanov.pythonanywhere.com/auth/token/login/`

Logout:
**POST** `http://khasanov.pythonanywhere.com/auth/token/logout/`
