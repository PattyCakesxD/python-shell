import sys


def main():
    while True:
        cmd = input("$ ")

        if cmd == "exit":
            break
        elif cmd[:5] == "echo ":
            print(cmd[5:])
        else:
            print(f"{cmd}: command not found")

        

if __name__ == "__main__":
    main()
