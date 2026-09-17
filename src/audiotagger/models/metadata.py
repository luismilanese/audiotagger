from dataclasses import dataclass
from pathlib import Path

from audiotagger.models import formats


@dataclass
class AudioMetadata:
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    track_number: str | None = None
    year: str | None = None


@dataclass
class RenameResult:
    original_path: Path
    new_path: Path
    success: bool
    error_message: str | None


@dataclass
class AudioFileContext:
    file_format: formats.FormatsSupported
    file_path: Path
