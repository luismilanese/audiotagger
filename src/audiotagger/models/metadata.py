from dataclasses import dataclass


@dataclass
class AudioMetadata:
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    track_number: str | None = None
    year: str | None = None
