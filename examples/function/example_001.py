
def subfunc():
    print("subfunc called:")


def main():
    print("main called:", __name__)
    subfunc()

if __name__ == "__main__":
    main()

print("exit")