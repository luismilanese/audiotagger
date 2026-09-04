from enum import Enum

from mutagen.easyid3 import EasyID3


class FormatsAllowed(Enum):
    MP3 = ".mp3"
    FLAC = ".flac"
    OGG = ".ogg"


class Format:
    pass


class Mp3(EasyID3, Format):
    def __init__(self, filename=None):
        super().__init__(filename)


class AudioFileContext:
    def __init__(self, format, file_path) -> None:
        self.format = format
        self.file_path = file_path


class AudioFileFactory:
    @staticmethod
    def create_audio_file(context: AudioFileContext):
        if context.format == FormatsAllowed.MP3:
            return Mp3(context.file_path)
        else:
            raise ValueError("Invalid file type")
