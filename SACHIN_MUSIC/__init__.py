from SACHIN_MUSIC.core.bot import SACHIN
from SACHIN_MUSIC.core.dir import dirr
from SACHIN_MUSIC.core.git import git
from SACHIN_MUSIC.core.userbot import Userbot
from SACHIN_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SACHIN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
