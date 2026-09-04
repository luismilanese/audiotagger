from pathlib import Path

from audiotagger.models.formats import (
    AudioFileContext,
    AudioFileFactory,
    FormatsAllowed,
)
from audiotagger.utils import extract_tracknumber


def format_guess(file_path: str) -> FormatsAllowed | None:
    if not Path(file_path).is_file():
        return None

    for fmt in FormatsAllowed:
        if file_path.lower().endswith(fmt.value):
            return fmt
    return None


def rename(file_path: Path):
    guessed_format = format_guess(str(file_path))
    if not guessed_format:
        return

    file_context = AudioFileContext(guessed_format, file_path)
    audio_file = AudioFileFactory.create_audio_file(file_context)
    mask = f"{extract_tracknumber(audio_file.get('tracknumber')[0])} - {audio_file.get('title')[0]}.mp3"
    destination_folder = file_path.parent
    new_file_path = f"{destination_folder}/{mask}"
    file_path.rename(new_file_path)
