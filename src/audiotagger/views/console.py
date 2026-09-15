from audiotagger.models.metadata import RenameResult


class FontStyles:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


class ConsoleView:
    @staticmethod
    def display_results(results: list[RenameResult], is_dry_run: bool):
        errors = 0
        successes = 0

        if is_dry_run:
            print(
                f"{FontStyles.YELLOW}[Preview Mode]: No changes have been written to disk. Use {FontStyles.BOLD}--apply{FontStyles.RESET} {FontStyles.YELLOW}to write them.{FontStyles.RESET}"
            )

        for rename_result in results:
            if rename_result.error_message:
                errors += 1
                print(
                    f"{rename_result.original_path.name} ➔ {FontStyles.RED}[ERROR]: {rename_result.error_message}{FontStyles.RESET}\n"
                )
                continue

            successes += 1

            if rename_result.original_path == rename_result.new_path:
                print(
                    f"{FontStyles.BOLD}Old file name: {rename_result.original_path.name}{FontStyles.RESET}\nNew file name: {rename_result.new_path.name} {FontStyles.CYAN}[NO CHANGES]{FontStyles.RESET}\n"
                )
                continue

            print(
                f"{FontStyles.BOLD}Old file name: {rename_result.original_path.name} \nNew file name: {rename_result.new_path.name}\n"
            )

        print("=" * 50)
        print("Files processed:     ", len(results))
        print("Successfully renamed:", successes)
        print("Errors:              ", errors)
