import re


def extract_tracknumber(tracknumber: str) -> str:
    match = re.search(r"^\d+", tracknumber.strip())
    if match:
        return match.group()
    return ""
