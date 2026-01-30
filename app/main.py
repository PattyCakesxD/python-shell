import sys


def main():
    while True:
        cmd = input("$ ")

        if cmd == "exit":
            break
        else:
            print(f"{cmd}: command not found")

        

if __name__ == "__main__":
    main()
