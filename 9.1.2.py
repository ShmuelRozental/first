path = input("please enter a file path")
task = input("please enter a task")
with open(path, "r") as text_file:
    if task == "sort":
        reed_text = text_file.read()
        words = reed_text.split()
        unique_words = list(set(words))
        unique_words.sort()
        print(words)
        print(unique_words)
    if task == "rev":
        for line in text_file:
            print(line[::-1])
    if task == "last":
        num = int(input("please enter a num of last line that you wont print"))
        reed_text = text_file.readlines()
        print(reed_text[num:])











var = open(r"C:\Users\Win10\Downloads\sampleFile.txt.txt",'r')