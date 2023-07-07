```python
import requests
from user_management import user

# Define the URLs for the social media APIs
FACEBOOK_API_URL = "https://graph.facebook.com/v12.0/me/photos"
TWITTER_API_URL = "https://api.twitter.com/1.1/statuses/update_with_media.json"
INSTAGRAM_API_URL = "https://api.instagram.com/v1/media/upload"

def share_on_facebook(meme):
    # Get the user's Facebook access token
    access_token = user.get_facebook_access_token()

    # Prepare the payload
    payload = {
        "url": meme.url,
        "caption": meme.caption,
        "access_token": access_token
    }

    # Send a POST request to the Facebook API
    response = requests.post(FACEBOOK_API_URL, data=payload)

    # Check the response
    if response.status_code == 200:
        print("Meme shared on Facebook successfully!")
    else:
        print("Failed to share meme on Facebook.")

def share_on_twitter(meme):
    # Get the user's Twitter access token and secret
    access_token, access_token_secret = user.get_twitter_access_tokens()

    # Prepare the payload
    payload = {
        "status": meme.caption,
        "media": meme.url
    }

    # Send a POST request to the Twitter API
    response = requests.post(TWITTER_API_URL, data=payload, auth=(access_token, access_token_secret))

    # Check the response
    if response.status_code == 200:
        print("Meme shared on Twitter successfully!")
    else:
        print("Failed to share meme on Twitter.")

def share_on_instagram(meme):
    # Get the user's Instagram access token
    access_token = user.get_instagram_access_token()

    # Prepare the payload
    payload = {
        "image_url": meme.url,
        "caption": meme.caption,
        "access_token": access_token
    }

    # Send a POST request to the Instagram API
    response = requests.post(INSTAGRAM_API_URL, data=payload)

    # Check the response
    if response.status_code == 200:
        print("Meme shared on Instagram successfully!")
    else:
        print("Failed to share meme on Instagram.")
```