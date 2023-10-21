def copy_file_content(source, destination):
    with open(source, "r") as reed_file:
        with open(destination,"w") as copy_file:
            copy_file.write(reed_file.read())




copy_file_content(r"C:\Users\Win10\PycharmProjects\pythonProject\bark class\copy.txt", r"C:\Users\Win10\PycharmProjects\pythonProject\bark class\chat.txt")