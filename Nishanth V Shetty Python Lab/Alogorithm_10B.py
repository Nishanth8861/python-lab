def clear_file(filename):
    try:
        file = open(filename, "w")   # 'w' mode clears file
        file.close()
        print("File data cleared successfully!\n")

    except Exception as e:
        print("Error:", e)


def check_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()

    if not data:
        print("File is now empty\n")
    else:
        print("File still has data\n")


def main():
    filename = "students.txt"

    print("Clearing file data...")
    clear_file(filename)

    print("Checking file...")
    check_file(filename)


if __name__ == "__main__":
    main()
