import argparse
from pathlib import Path

from audiotagger.models.exceptions import InvalidPathException
from audiotagger.models.file_handling import FileRenamer
from audiotagger.views.console import ConsoleView


class CLIController:
    @staticmethod
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("path", type=Path, help="location of the file or folder")
        parser.add_argument(
            "-m",
            "--mask",
            type=str,
            default="%artist% - %track_number% - %title%",
            help="mask pattern files will be renamed to (default: %%artist%% - %%track_number%% - %%title%%)",
        )
        parser.add_argument(
            "-a", "--apply", action="store_true", help="write the changes to disk"
        )
        args = parser.parse_args()
        try:
            renamed_files = FileRenamer.rename_all(args.path, args.mask, not args.apply)
            ConsoleView.display_results(renamed_files, not args.apply)
        except InvalidPathException as e:
            ConsoleView.display_errors(str(e))
