import os

class Config:
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
    SESSION_NAME = os.environ.get("SESSION_NAME", "userbot")  # Keep this short
    SESSION_STRING = os.environ.get("SESSION_STRING", "")  # For string sessions
    OWNER_ID = int(os.environ.get("OWNER_ID", 123456789))
    
    SUDO_USERS = {OWNER_ID}
    SUDO_USERS_FILE = "sudo_users.txt"
