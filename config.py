# Don't Remove Credit @BRPXLHACKING
# Subscribe YouTube Channel For Amazing Bot @HEART_HACKERBIO
# Ask Doubt on telegram @HEART_HACK3R_149


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "17633660")

API_HASH = os.environ.get("API_HASH", "550d6be4e103078e66af28e87bca0a6f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7778976653:AAEi5fMyytw_xxvdVQmHxzcDCRObN_Zo-nY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "BRPXLHACKING") 

             # Don't Remove Credit @HEART_HACKERBIO
             # Subscribe YouTube Channel For Amazing Bot @HEART_HACKERBIO
             # Ask Doubt on telegram @HEART_HACK3R_149

DB_NAME = os.environ.get("DB_NAME", "brpxlrenamebot")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6267674324').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @BRPXLHACKING
# Subscribe YouTube Channel For Amazing Bot @HEART_HACKERBIO
# Ask Doubt on telegram @HEART_HACK3R_149
