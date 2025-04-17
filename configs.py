# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27419615"))
    API_HASH = getenv("API_HASH", "2f4b181296f0a2615a85471a1c72df44")
    BOT_TOKEN = getenv("BOT_TOKEN", "7583971283:AAFkxo3xyKDFQ4hFdvnUvGwl3xeICU5J84k")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002203224796")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1534632634").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rohitl3031:CNHkZh4Nkgv0mUuJ@cluster0.cgmci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
