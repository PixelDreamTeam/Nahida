
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27776767" # integer value, dont use ""
    API_HASH = "e7b0d8f7b037df9ff8b300816e90080b"
    TOKEN = "6358179443:AAHL_kb4fkNXcrcg7W0j_P45xHIZ8y6pwCI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6975932205 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "FlameBloodsUnion"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/02c3abd53e810a92d2f20.jpg"
    EVENT_LOGS = -1002049125216  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI = "mongodb+srv://roundnessxyz:K8gfBy7UABqI0cRL@nahida-database.1yubfvl.mongodb.net/?retryWrites=true&w=majority&appName=Nahida-database"
    # RECOMMENDED
    DATABASE_URL = "postgres://sdzssnho:yOsX_yr6nKBy4NeZWeI2hr8gmiUKsdOr@baasu.db.elephantsql.com/sdzssnho"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "NKOM6OH1IVLTUA86"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    
    # Get your API key from https://timezonedb.com/api


    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1463920223]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = [1450535848]  # User id of support users
    TIGERS = [5758389151]  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
