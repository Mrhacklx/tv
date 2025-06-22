
import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get('API_ID', '27382550'))
API_HASH = environ.get('API_HASH', 'c428034cb811de290315501d8e3c82b5')
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://i.ibb.co/27qXHP94/Whats-App-Image-2025-06-16-at-14-11-42-9af52d26.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6739173851').split()]
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Mr_attherate')
BOT_USERNAME = environ.get("BOT_USERNAME", "XYZGetModBot") # without @
PORT = environ.get("PORT", "8080")

PREMIUM_MODE = bool(environ.get('PREMIUM_MODE', True))
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://vault.pictures/media/images/94/89/aa/9489aa904a9f44bd8c92abdd908a6270.png') # payment code picture url.
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', """<b>💸 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐏𝐥𝐚𝐧𝐬 💸\n\n🔹 30₹ – 1 Month  \n🔹 100₹ – 5 Months  \n🔹 200₹ – 12 Months\n\n🎁 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 🎁\n\n✅ No verification needed  \n✅ No link opening required  \n📥 Direct file access  \n🚫 Ad-free experience    \n🛠️ Full admin support  \n⏱️ Requests completed within 1 hour (if available)\n\n✨ 𝐔𝐏𝐈 𝐈𝐃: <code>raxiecat@ybl</code>\n\n🔎 Check your plan here: /myplan\n\n📸 After payment, send a screenshot  \n⏳ Please wait patiently while we activate your premium access</b>""")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Information
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002849749742"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', True)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "shortxlinks.com") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "489acf90c4d4844bcbfddcf355ad155fabdda45c") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/How_to_Open0") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
