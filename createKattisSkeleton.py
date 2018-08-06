if __name__ == "__main__":
    file_name = input("What is the file name? ")

    with open("{}.py".format(file_name), "w") as f:
        f.write("class Problem:\n")
        f.write("    def __init__(self):\n")
        f.write("        pass\n\n\n")
        f.write('if __name__ == "__main__":\n')
        f.write("    pass\n")
