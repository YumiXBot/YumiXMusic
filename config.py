import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29326517"))
API_HASH = getenv("API_HASH", "3d4c0484ec90ebb88934b4320e80dff0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1000"))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001603822916"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6079943111"))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/YumiXBot/YumiXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AlonesHeaven")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", "BQCzTb8AA-SZSIE8wz-R94YaQR-nL9bAqp4y95uzN5Gbj5jhWthQnSvkaXN1hOH1UXs-G4sGaRWn16lcsiDdZvyO_hfv4CXCrVyGuONahy4zazcBfzd3BwIE_siq4LQKenhYUHGl9nPbpco00cLwDH6_NvL9NjUId2Ho5a8QZFnTpbuN7oIchLvFxXpgMHEKPUulfx2zVO8SW_irBKRYPtSXRObKbA-hKIQrnuN4NkpSiVA1PjHQeJXt9fKURKwyH2aJQDvrRQXL2Nq0RV_a_xfa6KsezDeOsyS7MZySoBeIrqB692xhR4g0jz-TC5hhUvNTmQHIdrpYUT2KyFip61y7HtUWogAAAABqwr10AA")
STRING3 = getenv("STRING_SESSION3", "BQDZ6zQAPbEgXhGXDGVTNToM1zxT9TOMl78UMpaLNqYTO5Y_23fQ7A0bID6AQQgnf38WrlDarmQpnirhoNhynEl34GzTffn_4It1qN4DPKMjCIEG2LCzKbxwKLaIWDJ39DSJU_MzFtIAMOCzteg7UTB08KAYddNagonUourqgV8SDxrgMlhpBpYjNyMQrtWs9dRl0Ve8brMhPyVqdcc5EfMMV0KF3dnFEd_mPq8sjvq3qAhgEZKM2WozPE7-8NMRSkWOv9XZMCs6UW_nHENXfZgfftD1fipVZCUewemIoAiXgENFyRTZYRsUzEmaxacTTNeWCARKcrPUNcszujE-q_0J7lQtYgAAAAFbFbFxAA")
STRING4 = getenv("STRING_SESSION4", "BQG7300ACNYsQ20fCFYFc0upiWDutKUJN0C74r26Hp3S4H0jCqL2ucPpy9GuJ0ngtN3fMJjwUujKKn3O3y1Hg8jZBcvSJPWbOfauJeTzPdZoRwrMRwtuY9kYU9g7Pu6_1kTvqR06T1CQDGQX9Vnois58SJmPPuXc8rt5PhK72CqHPUuhU3YLvMIDvlzb_JcjKPAY1JVhiO_HXxbt3qlbMyg_M1LgUHTdpNZ8ugzT3H6_m0z2UONWTRCsBa9zyBM2d1d_g-oM2UlviUi5xj8fXB3zFY_5o3_RmhmOtnaOptuT3UuwUpCbMLAMIHN52ui96Z3dloijKslA2zwtxiN8B1knKdCIXQAAAAFvHw8EAA")
STRING5 = getenv("STRING_SESSION5", "BQEMf1sAPgC9w3u1M4z19TxqYWioQ8lNUYOBt6SzJn5sJprUJk2RbET8cTkl5MaaJVe_OtPAu29I4Xzujmd3hOLUDXo0utPqhb8D68kov-0WRUQvgIwxfhUQne3lHGgO8rxxUhuQRwIQryslVuRcoIvtckNX_2LAMg2aSalSeOlBRR_Hw-0UOqRCpPNjDxC0XGxgQeXaEmjTuiEZln_8zH4G0XuMQwkndCpv-50kis6AHzlSGKWJug1P1YJ6p7bu12PXjaEik01Y7gfkloSzB2AWuBgrMcS6Y26kUr_e_bIj9VYbRwA3Qxi9dyDjsr6h_CzyDcxaSGINhMdTE82O6iY3G23WdAAAAAF2AZtFAA")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png"]
PING_IMG_URL = ["https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png"]
STATS_IMG_URL = ["https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
