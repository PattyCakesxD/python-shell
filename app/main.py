import sys

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
            if res[1] in VALID_FUNCTIONS:
                print(f"{res[1]} is a shell builtin")
            else:
                print(f"{res[1]}: not found")
        else:
            print(f"{cmd}: command not found")
        

if __name__ == "__main__":
    main()
