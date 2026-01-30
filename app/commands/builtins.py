from commands import utils
import os

def run_echo(args):
    ### Outputs contents after echo command ###
    print(" ".join(args))


def run_type(args):
    ### Outputs path to command if it exists and isn't a shell builtin function (use find_PATH to return only the directory) ###
    if not args:
        return
    
    for arg in args:
        if arg in COMMAND_REGISTRY:
            print(f"{arg} is a shell builtin")
            continue
        
        path = utils.find_PATH(arg)

        if path:
            print(f"{arg} is {path}")
        else:
            print(f"{arg}: not found")


def run_pwd(_):
    ### Output absolute path of current working directory ###
    print(os.getcwd())

COMMAND_REGISTRY = {
    "echo": run_echo,
    "type": run_type,
    "pwd": run_pwd,
}