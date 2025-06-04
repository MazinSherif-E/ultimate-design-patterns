from VideoProvider import VideoProvider
from VideoQuality import VideoQuality

class YoutubeVideoProvider(VideoProvider):
    def __init__(self, quality: VideoQuality):
        self.quality = quality
        
    def playback(self) -> str:
        self.quality.render()
        return "Youtube Video Playback"