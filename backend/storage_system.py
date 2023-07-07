```python
import os
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['video_meme_generator']

# Collections
users = db['users']
videos = db['videos']
memes = db['memes']

# File storage path
storage_path = "/path/to/storage/directory"

def save_file(file, filename):
    file_path = os.path.join(storage_path, filename)
    file.save(file_path)
    return file_path

def save_user(user):
    users.insert_one(user)

def get_user(user_id):
    return users.find_one({"_id": user_id})

def update_user(user):
    users.update_one({"_id": user["_id"]}, {"$set": user})

def delete_user(user_id):
    users.delete_one({"_id": user_id})

def save_video(video):
    videos.insert_one(video)

def get_video(video_id):
    return videos.find_one({"_id": video_id})

def update_video(video):
    videos.update_one({"_id": video["_id"]}, {"$set": video})

def delete_video(video_id):
    videos.delete_one({"_id": video_id})

def save_meme(meme):
    memes.insert_one(meme)

def get_meme(meme_id):
    return memes.find_one({"_id": meme_id})

def update_meme(meme):
    memes.update_one({"_id": meme["_id"]}, {"$set": meme})

def delete_meme(meme_id):
    memes.delete_one({"_id": meme_id})
```