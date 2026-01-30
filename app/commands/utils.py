import subprocess
import os

def run_exe(cmd, args, path):
    ### Runs a custom executable along with its args ###
    try:
        res = subprocess.run([cmd] + args, executable=path)
        return res
    except subprocess.CalledProcessError as e:
        pass # TODO: Handle error if it comes up

def find_PATH(cmd):
    ### Returns path to command if it exists ###
    PATH = os.environ.get("PATH", "")

    for p in PATH.split(os.pathsep):
        res = os.path.join(p, cmd)

        if os.path.isfile(res) and os.access(res, os.X_OK):
            return res
    
    return None

