# Starnavi(middle)
## Django project (Social Network realization)

### Requirements:
* Signup user
* Login user
* Post creation
* Post like
* Post dislike
* Aggregated analytics by day (period) of how many likes was made by user
* Last seen
* JWT access token

### Models:
* User
* Post

### My realization:
1) Changed basic Django app files structure.
2) Changed **id** field of the models to the uuid .
3) Moved all similar fields of the models into the abstract.
4) Created Choice(Enum) class for choices readability (_LikeTypeChoice_).
5) Aggregating likes by period (day, month, year and quarter) and simplified function. It was made to make Frontend devs work easier to draw graph from back.
6) Added custom middleware to handle last_seen (request).