import os

class Config:
    API_ID = int(os.environ.get("API_ID", 21505404))
    API_HASH = os.environ.get("API_HASH", "5feffdf4111ed339381056d9476d3fcd")
    SESSION_NAME = os.environ.get("SESSION_NAME", "userbot")  # Keep this short
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQFIJXwAAdn1faEgOgMIaxRqxA-V3hCegwb73BZtS-y7KRHojtsfw1BObsqq7WpSpsTWf1zn38GNw_XwU0eFayR_6P8qRCpffWG5vBYq3phbec_kemFL5zyCHTkakgiGe24iXHuu20WjjOM38qnAzArbyHJ37wBnWCto-xfzxGaZrDKtPTFaj0-FXj6U1fuoN7RLD-niPOMSam2pncYNPV9tR6zGBjSo1RFqgLewpGgzefM__nP_0KQLaoGT-m8VfT2Agn5pLMgKejpqoMjUq-xaRh8ADFk1MkC5Heo5QM-bXZzqmE2nBmCjFxRzhwntCmmwa-TYtk0xD9Gc7jfGuqwpEfYIFwAAAAGEf7yQAA")  # For string sessions
    OWNER_ID = int(os.environ.get("OWNER_ID", 6061153252))
    
    SUDO_USERS = {OWNER_ID}
    SUDO_USERS_FILE = "sudo_users.txt"
