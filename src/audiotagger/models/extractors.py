from pathlib import Path

from audiotagger.models.formats import (
    AudioFileContext,
    AudioFileFactory,
    FormatsAllowed,
)
from audiotagger.models.metadata import AudioMetadata


def detect_format(file_path: str) -> FormatsAllowed | None:
    if not Path(file_path).is_file():
        return None

    for fmt in FormatsAllowed:
        if file_path.lower().endswith(fmt.value):
            return fmt
    return None


class InvalidAudioFileException(Exception): ...


class AudioFileMetadataExtractor:
    @staticmethod
    def extract(file_path: Path) -> AudioMetadata:
        format_detected = detect_format(str(file_path))
        if format_detected == None:
            raise InvalidAudioFileException(f"invalid audio file: {file_path}")

        audio_file_context = AudioFileContext(format_detected, file_path)
        audio = AudioFileFactory.create_audio_file(audio_file_context)

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
