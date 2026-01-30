import subprocess
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
            print(check_type(res[1]))
        else:
            # Run custom exe if it exists in PATH
            path_dir = find_PATH(cmd)

            if path_dir:
                run_exe(cmd, path_dir, res[1:])
            else:
                print(f"{cmd}: command not found")

def check_type(cmd):
    ### Outputs path to command if it exists and isn't a shell builtin function (use find_PATH to return only the directory) ###
    if (cmd) in VALID_FUNCTIONS:
        return f"{cmd} is a shell builtin"

    PATH = os.environ.get("PATH", "")

    for p in PATH.split(os.pathsep):
        res = os.path.join(p, cmd)

        if os.path.isfile(res) and os.access(res, os.X_OK):
            return f"{cmd} is {res}"
    
    return f"{cmd}: not found"

def find_PATH(cmd):
    ### Returns path to command if it exists ###
    PATH = os.environ.get("PATH", "")

    for p in PATH.split(os.pathsep):
        res = os.path.join(p, cmd)

        if os.path.isfile(res) and os.access(res, os.X_OK):
            return res
    
    return None

def run_exe(cmd, path, args):
    try:
        res = subprocess.run([cmd] + args, executable=path)
        return res
    except subprocess.CalledProcessError as e:
        pass



if __name__ == "__main__":
    main()
