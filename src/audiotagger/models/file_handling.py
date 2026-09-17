from pathlib import Path

from mutagen import MutagenError

from audiotagger.models.exceptions import (
    InvalidAudioFileException,
    InvalidPathException,
)
from audiotagger.models.extractors import AudioFileMetadataExtractor
from audiotagger.models.formats import FormatsSupported
from audiotagger.models.mask import MaskEngine
from audiotagger.models.metadata import RenameResult


class FileRenamer:
    @staticmethod
    def rename(file_path: Path, mask: str, dry_run: bool = True) -> RenameResult:
        try:
            audio_metadata = AudioFileMetadataExtractor.extract(file_path=file_path)
        except (MutagenError, InvalidAudioFileException, OSError) as e:
            return RenameResult(
                original_path=file_path,
                new_path=file_path,
                success=False,
                error_message=str(e),
            )

        new_name = MaskEngine.apply(mask, audio_metadata)
        new_path = file_path.with_name(f"{new_name}{file_path.suffix}")

        rename_result = RenameResult(
            original_path=file_path,
            new_path=new_path,
            success=True,
            error_message=None,
        )

        if file_path == new_path:
            return rename_result

        if new_path.exists():
            return RenameResult(
                original_path=file_path,
                new_path=file_path,
                success=False,
                error_message="there is a file with this name already",
            )

        if dry_run:
            return rename_result

        try:
            file_path.rename(new_path)
            return rename_result
        except OSError as e:
            return RenameResult(
                original_path=file_path,
                new_path=file_path,
                success=False,
                error_message=str(e),
            )

    @classmethod
    def rename_all(
        cls, path: Path, mask: str, dry_run: bool = True
    ) -> list[RenameResult]:

        if not path.is_file() and not path.is_dir():
            raise InvalidPathException("the provided path isn't a file or a directory")

        result = []
        if path.is_file():
            ret = cls.rename(path, mask, dry_run)
            result.append(ret)
            return result

        if path.is_dir():
            audio_files = [
                f
                for f in path.iterdir()
                if f.is_file() and f.suffix.lower() in FormatsSupported
            ]
            for audio_file in audio_files:
                ret = cls.rename(audio_file, mask, dry_run)
                result.append(ret)

        return result
