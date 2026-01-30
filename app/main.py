import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from commands import builtins, utils

def main():
    while True:
        userInput = input("$ ")
        res = userInput.split()
        if not res: continue

        cmd_name = res[0]
        args = res[1:]

        if cmd_name in builtins.COMMAND_REGISTRY:
            builtins.COMMAND_REGISTRY[cmd_name](args)

        else:
            # Run custom exe if it exists in PATH
            path = utils.find_PATH(cmd_name)

            if path:
                utils.run_exe(cmd_name, res[1:], path)
            else:
                print(f"{cmd_name}: command not found")


if __name__ == "__main__":
    main()
