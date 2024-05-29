def main():
    try:
        conf = open("config.text")
        print(f"TRUE {conf}")
    # except FileNotFoundError:
    #     print("none file")
    except IsADirectoryError:
        print("Found Config")
    except OSError as err:
        if err.errno == 2:
            print("errno")
        elif err.errno == 13:
            print("it")

if __name__ == "__main__":
    main()