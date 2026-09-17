import re

from audiotagger.models.metadata import AudioMetadata

MASK_MAPPING = {
    "%artist%": "artist",
    "%title%": "title",
    "%album%": "album",
    "%year%": "year",
    "%track_number%": "track_number",
}


class MaskEngine:
    @staticmethod
    def apply(mask: str, metadata: AudioMetadata) -> str:
        resolved = MaskEngine._resolve_tokens(mask, metadata)
        sanitized = MaskEngine._sanitize_filename(resolved)
        return sanitized

    @staticmethod
    def _resolve_tokens(mask: str, metadata: AudioMetadata) -> str:
        def replace_token(match: re.Match[str]) -> str:
            token = match.group(0)
            attribute = MASK_MAPPING.get(token)
            if attribute is None:
                return token

            return str(getattr(metadata, attribute, "") or "")

        return re.sub(r"%[^%]+%", replace_token, mask)

    @staticmethod
    def _sanitize_filename(filename: str) -> str:
        pattern = r'[\\/:*?"<>|]+'
        sanitized = re.sub(pattern, " ", filename).strip()
        if sanitized.endswith("."):
            sanitized = sanitized[0:-1]
        return sanitized
