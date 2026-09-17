from enum import Enum
from pathlib import Path

import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC

from audiotagger.models.exceptions import (
    InvalidAudioFileException,
    InvalidPathException,
)
from audiotagger.models.metadata import AudioFileContext


class FormatsSupported(Enum):
    MP3 = ".mp3"
    FLAC = ".flac"
    OGG = ".ogg"


def detect_format(file_path: str) -> FormatsSupported:
    if not Path(file_path).is_file():
        raise InvalidPathException("invalid file")

    for fmt in FormatsSupported:
        if file_path.lower().endswith(fmt.value):
            return fmt

    raise InvalidAudioFileException("file format not supported")


class AudioFileFactory:
    @staticmethod
    def create_audio_file(context: AudioFileContext):
        if context.file_format == FormatsSupported.MP3:
            return EasyID3(context.file_path)
        elif context.file_format == FormatsSupported.OGG:
            return mutagen.File(context.file_path, easy=True)
        elif context.file_format == FormatsSupported.FLAC:
            return FLAC(context.file_path)
