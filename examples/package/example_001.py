import pkg.samplepkg
from pkg.samplepkg_sub import samplepkg_sub_func


def main():
    print("main called:", __name__)
    pkg.samplepkg.samplepkg_func()
    samplepkg_sub_func()

if __name__ == "__main__":
    main()

print("done")