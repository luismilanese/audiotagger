from pathlib import Path
from typing import Protocol

from mutagen.easyid3 import EasyID3

from audiotagger.models.metadata import AudioMetadata


class MetadataExtractor(Protocol):
    def extract(self, file_path: Path) -> AudioMetadata: ...


class MP3MetadataExtractor:
    @staticmethod
    def extract(file_path: Path) -> AudioMetadata:
        audio = EasyID3(file_path)

        def get_first(key: str) -> str | None:
            values = audio.get(key)
            return values[0].strip() if values else None

        track_number = get_first("tracknumber")
        track_number_clean = (
            track_number.split("/")[0].strip() if track_number else None
        )

        return AudioMetadata(
            title=get_first("title"),
            artist=get_first("artist"),
            album=get_first("album"),
            track_number=track_number_clean,
            year=get_first("date"),
        )
