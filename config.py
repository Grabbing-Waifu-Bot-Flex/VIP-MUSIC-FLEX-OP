import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "14691251"))
API_HASH = getenv("API_HASH", "ce7153b02b496253947872656b3ee0d3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6999969950:AAGIwlgqnDowSBew4yBuvbpDOeIEuaxPLBg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mukundsrajput:lFRam73ZwE2D4snZ@cluster0.bmxejth.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002078575375"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002078575375"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6584789596"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Flex_Bots_News")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Flex_Support_Chat")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQDgK7MAJjGG8P0Wt66LvepDxNxK_XH7R-xBDL_6kwVVOEn495oLwcGcpx1kAoJW7Wh7oMdqvcPmXIucADpyOJGiWbp8RXo06foNhexDuYFK7p_ijkVs9h2rRv6AsSdQELCsKNTYUtK-GEzfbNIBwWIHLdQCfKQ3KUYeU-U2_wq6VvVSSiqyP1eth9Cu7i01DJCmUS932cnrTIegFVJLG7Oo6Rd0YmtmLd2XiwowlqP_-1iAvqhjvePh5kJqdM_Ov-S9erPBF1MRNR6osRqP7ZxCQMpdtCufVGClIEmJr_fE3Gi_lJjyZOqyAqqJfANW06K4bxGTQXZ_m4LEvLlJM913qV7VygAAAAGlYLD2AA")
STRING2 = getenv("STRING_SESSION2", "BQDgK7MAwDdhoFepSlSuLofcUCmm6wyRf8JsJ_O59AemNC8t36YwC-VyLAZkf7FJ8dcDw7bW8PHcHiC9jiXmm3Rb2hvdq6tov6mYliJCui4CicGYrGZTgcmCi5RUivDoNNKb3BSOjDGbVuJLU_nP_qoxzNKca7b32_PZxwl3GWX2qDToKjlowd5YXqwrgQ-T63lcRQQ-5TRrmexbHJ2S1MVnRrfyDDMzUfXDmzgdL9tlrUZnnPa5FqO-cwArBQz94AsGegrEZOra-EbiB55gldrEr6lwrIi92sOlET8V8m4HPvNy4f5gLFlonqsdaAOqlvb_QdTTYIi-9ZiFcO2pUp3Tp-DokQAAAAGlYLD2AA")
STRING3 = getenv("STRING_SESSION3", "BQDgK7MABVuTMczYGchsjuoCt7wAyPCwlM1HrPHgPc9ohD9EKztYvFX66yKZCOY8sKEq47Qi3T_Ic47kVYtHj2v4W_BFIS2_mspRqUR2D0Dnw2V-zaW3M4CdCnkDkoFWXBz-zZkZWAhjax8wNzWEdxPqjz1Br7CY-Fgxq9E0KB3nVuQGAH1gqO_dL4n5oah0yOdi1teYA5aJRmWUl4bHILdL8AQHqp0tdlYWDhBCbhOeZm8ikyEnhgY9-pHB6ld_n-IulmeRE_FkcPqj6Mcfvo6MyZa0cNTpigefS2eyVpM2eQlCp2iPyZU-r-_8Eq6hnKqhiTJYjwmpsKHzr0TUbe6NsnoV4AAAAAGlYLD2AA")
STRING4 = getenv("STRING_SESSION4", "BQDgK7MAg5UU_-62yvg-9WjQnJIgjjreaqNdCwYNj28lqAgD7Rqys8s24RnDWOmwMFAbIluk3hiPbEZJu4UAKkAdlexGv1vtC0cjXJXM2yNUwUVGlAmhsNva-Xz_hK0vxzBdGJra1c1lX8KY4U4QJE4qmnLVVJli2Y5En-zFkg419SnnPLU4lOQOERF68HMEwLr7daL22aO5tKc3eft9a4PmQ1B8gBYyVxmsmRMEB_oWNxKltMBBfseDC9lY3K-9a5uz5ebUX9viraVZZ6LzZg1G0cSDVGIQe51fegF-FdijWiJ3q854z5LUZDUrCiOxWkAnOcW7PztxGCuL4W6XyqRfFjkgAAAAGlYLD2AA")
STRING5 = getenv("STRING_SESSION5", "BQDgK7MADxmU6Ig4sSSohP0CctA9MytPJy5PYxn-O6C3QXo7RSOgT2Ooq5Ohnmw1iHfb46NJHa0cAOHSdNrL8nFjneuJ3G9n_Jrn4bHwSMn3eqA2YH3OOs4Y0Mt3SiGnAd4evLTAAhBSLop-797B3-7UlTCSVKZIPtMDEnWQPqLfjnjrZUNTh_eFZC2nUYqKp7-x1yJ16H5qtgagnZMz-zsDtTR0AJxBmwCmcCv8fCRMcOKGSMuREQjIdKZbTdBFymqMM3TCG5Ns7IMiGulkInXGBzZ-2qIfQG2uSimg64PfDXg6f8GI7UlskgxtUwgN15ICVue_nZhO78An6mMz6sDH6SjLtAAAAAGlYLD2AA")


#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____   ____ _______
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __|
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/af76565ecb93f1763a9fd.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
STATS_IMG_URL = "https://graph.org/file/527daa229a210ec5b901f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
STREAM_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
