from pathlib import Path
import os
import time

from rich.console import Console
from rich.progress import Progress

from rich.table import Table

folder = Path("/home/manahu/Downloads/")
console = Console()


def main():

    table = Table()
    table.add_column("files that were affected")
    file_length = len([file for file in folder.iterdir() if file.is_file()])

    with Progress() as progress:
        task = progress.add_task("men in work...", total=file_length)

        for file in folder.iterdir():
            suffix = file.suffix
            table.add_row("")
            table.add_row(file.name)

            if suffix in [".jpg", ".jpeg", ".png"]:
                os.system(f"mv {file} ~/Downloads/Images/")

                time.sleep(1)
                print()
                print("-------------------------------------------")
                print(f"moved {file.name} to the 'Images' directory.")
                print("-------------------------------------------")
                print()
            elif suffix in [".txt", ".pdf", ".md"]:
                os.system(f"mv {file} ~/Downloads/Text")

                time.sleep(1)
                print()
                print("-------------------------------------------")
                print(f"moved {file.name} to the 'Text' directory.")
                print("-------------------------------------------")
                print()

            elif suffix in [".css", ".js", ".lua", ".py", ".gd", ".go", ".c", ".cpp"]:
                os.system(f"mv {file} ~/Downloads/Scripts")

                time.sleep(1)
                print()
                print("-------------------------------------------")
                print(f"moved {file.name} to the 'Scripts' directory.")
                print("-------------------------------------------")
                print()

            elif suffix in [".zip", ".7zip"]:
                os.system(f"mv {file} ~/Downloads/Zips")

                time.sleep(1)
                print()
                print("-------------------------------------------")
                print(f"moved {file.name} to the 'Zips' directory.")
                print("-------------------------------------------")
                print()

            progress.advance(task)

    console.print(table)


main()
