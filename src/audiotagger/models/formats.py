from enum import Enum

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis


class FormatsAllowed(Enum):
    MP3 = ".mp3"
    FLAC = ".flac"
    OGG = ".ogg"


class Mp3(EasyID3):
    def __init__(self, filename=None):
        super().__init__(filename)


class Ogg(OggVorbis):
    def __init__(self, filename=None):
        super().__init__(filename)


class Flac(FLAC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AudioFileContext:
    def __init__(self, format, file_path) -> None:
        self.format = format
        self.file_path = file_path


class AudioFileFactory:
    @staticmethod
    def create_audio_file(context: AudioFileContext):
        if context.format == FormatsAllowed.MP3:
            return Mp3(context.file_path)
        elif context.format == FormatsAllowed.OGG:
            return Ogg(context.file_path)
        elif context.format == FormatsAllowed.FLAC:
            return Flac(context.file_path)
        else:
            raise ValueError("Invalid file type")
