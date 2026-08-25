from pathlib import Path
import os
import time

folder = Path("/home/manahu/Downloads/")


def main():

    for file in folder.iterdir():
        suffix = file.suffix

        if suffix in [".jpg", ".jpeg", ".png"]:
            os.system(f"mv {file} ~/Downloads/Images/")

            time.sleep(2)
            print()
            print("-------------------------------------------")
            print(f"moved {file.name} to the 'Images' directory.")
            print("-------------------------------------------")
            print()
        elif suffix in [".txt", ".pdf", ".md"]:
            os.system(f"mv {file} ~/Downloads/Text")

            time.sleep(2)
            print()
            print("-------------------------------------------")
            print(f"moved {file.name} to the 'Text' directory.")
            print("-------------------------------------------")
            print()

        elif suffix in [".css", ".js", ".lua", ".py", ".gd", ".go", ".c", ".cpp"]:
            os.system(f"mv {file} ~/Downloads/Scripts")

            time.sleep(2)
            print()
            print("-------------------------------------------")
            print(f"moved {file.name} to the 'Scripts' directory.")
            print("-------------------------------------------")
            print()


main()
