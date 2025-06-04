from VideoQuality import VideoQuality

class FullHDVideoQuality(VideoQuality):
    def render(self) -> str:
        return "Full HD Video"