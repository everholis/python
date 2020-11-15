import module_001

def main():
    print("main called:", __name__)
    module_001.module_func()
    

if __name__ == "__main__":
    main()

print("exit")