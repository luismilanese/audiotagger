from pathlib import Path

from audiotagger.models import file_handling

folder = Path("/home/luis/Code/audiotagger/test_files")


files = [file for file in folder.iterdir() if file.is_file()]

for file in files:
    file_handling.rename(file)
