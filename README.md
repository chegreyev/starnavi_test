# Starnavi(middle)
## Automated bot
### Functionalities:
* Sign up users with **random** credentials
* Create post
* Like post
* Dislike post
* All changeble variables stored in **.env** file and Path for it could be changed

### User:
* API_URL - url to make requests
* headers - headers field to make requests with JWT access token
* register function - make request to register user with random email , first/last names and password
* create post - makes request to create post with a fixed name and description ( Could be changed to generating random text)
* get posts - used to get list of the posts and convert it list of post_id to make request to like/dislike
* like/dislike - makes request on a certain post to like or dislike it (but from my realization of liking/disliking)

*realization of liking and disliking posts - Post can't be liked twice or more times , furthermore if user disliked it before and liked it, dislike will change to like.