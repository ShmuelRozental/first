def are_files_equal(file1, file2):
    file_a = open(r"c:\file1.txt", "r").readlines()
    file_b = open(r"c:\file2.txt", "r").readlines()
    return file_a == file_b

