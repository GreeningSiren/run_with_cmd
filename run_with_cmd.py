import sys
import subprocess
from colorama import Fore, Back


def main():
    if len(sys.argv) > 1:
        # Get the first argument passed to the executable
        command = sys.argv[1]
        # Run the command with cmd
        print(Fore.CYAN + "Running:" + Fore.RESET)
        print(Back.RED + f'"{command}"' + Back.RESET + "\n")
#        subprocess.run(['cmd', '/c', command], shell=True)
        subprocess.run(command, shell=True)
    else:
        print("No command provided.")


if __name__ == "__main__":
    main()
