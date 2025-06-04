from YoutubeVideoProvider import YoutubeVideoProvider
from TwitchVideoProvider import TwitchVideoProvider
from HDVideoQuality import HDVideoQuality
from SDVideoQuality import SDVideoQuality
from FullHDVideoQuality import FullHDVideoQuality

hdVideoQuality = HDVideoQuality()
sdVideoQuality = SDVideoQuality()

youtubeVideoProvider = YoutubeVideoProvider(hdVideoQuality)
twitchVideoProvider = TwitchVideoProvider(sdVideoQuality)

youtubeVideoProvider.playback()
twitchVideoProvider.playback()