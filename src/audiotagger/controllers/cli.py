import argparse
from pathlib import Path

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
        renamed_files = FileRenamer.rename_all(args.path, args.mask, not args.apply)
        ConsoleView.display_results(renamed_files, not args.apply)


if __name__ == "__main__":
    CLIController.main()
