# Python Social Auth

## Inspiration:
Building SPAs and RestFul APIs in python frameworks like Django/ FastAPI/ Flask etc are a delight unless we encounter adding social login.
There is pretty good support for social login in Django for Templated apps using [Social-Core](https://github.com/python-social-auth/social-app-django) 
but this tends to be sticky to the templated applications and becomes confusing to provide a plain no Bull Shit approach to add a basic Google Social Login to the API, 

This is a fairly simple package with it's inital version supporting only Google Social Login since it's only thing I wanted to add in the APP I was building but it's open for contributions and feedback from the community to improve and add other providers.


To use it, 


```python
from nbs_social_auth.google import GoogleOAuth2

# Intialize the Google OAuth with the Credentials 

google_auth = GoogleOAuth2(GOOGLE_CLIENT_ID=<GOOGLE_CLIENT_ID>, GOOGLE_CLIENT_SECRET=<GOOGLE_OAUTH2_CLIENT_SECRET>,GOOGLE_REDIRECT_URI=<GOOGLE_CLIENT_SECRET>)


# Now we open up and endpoint to grab the AUTH URL on the APP
# In future we can add multiple providers and then send the AUTH URL based on a parameter 

@router.get("/social-auth-init-url")
def get_social_auth_url(request):


    return google_auth.get_auth_url()


```

Now the client recieves the auth URL and goes there to grab the auth credentials and we usually want it to redirect to a Frontned Page where we grab the auth token and then call the next API -> which would exchange the token with a JWT that is used across the API for authentication of the User

```python

@router.get("/check-social-auth-code")
def check_social_auth_code(request,code:str):
    try:
        social_user = google_auth.validate_code(code)
        email = social_user.get('email')

        # Register the User here / set provider / avatar-url or other parameters
        # Generate the token as per your logic here
        token =  jwt.encode({'email': email},SECRET, algorithm=algorithm)
        
        # Return the token, save on client side and use for subsequent authenticated requests 
        
    except Exception as e:
        # Handle the Error and pass a meaningful error message to the client 

```