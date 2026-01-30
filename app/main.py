import sys
import os

VALID_FUNCTIONS = ["exit", "echo", "type"]

def main():
    while True:
        userInput = input("$ ")
        res = userInput.split()
        cmd = res[0]

        if cmd == "exit":
            break
        elif cmd == "echo":
            print(" ".join(res[1:]))
        elif cmd == "type":
            print(check_PATH(res[1]))
        else:
            print(f"{cmd}: command not found")

def check_PATH(cmd):
    if (cmd) in VALID_FUNCTIONS:
        return f"{cmd} is a shell builtin"

    PATH = os.environ.get("PATH", "")

    for p in PATH.split(os.pathsep):
        res = os.path.join(p, cmd)

        if os.path.isfile(res) and os.access(res, os.X_OK):
            return f"{cmd} is {res}"
    
    return f"{cmd}: not found"
        

if __name__ == "__main__":
    main()
