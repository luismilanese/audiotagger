from pathlib import Path

from audiotagger.models.extractors import MP3MetadataExtractor
from audiotagger.models.mask import MaskEngine
from audiotagger.models.metadata import RenameResult


class FileRenamer:
    @staticmethod
    def rename(file_path: Path, mask: str, dry_run: bool = False) -> RenameResult:
        audio_metadata = MP3MetadataExtractor.extract(file_path=file_path)
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
            rename_result.success = False
            rename_result.error_message = "There is a file with this name already"
            return rename_result

        if dry_run:
            return rename_result

        try:
            file_path.rename(new_path)
        except OSError as e:
            rename_result.success = False
            rename_result.error_message = str(e)

        return rename_result
