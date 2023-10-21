def who_is_missing(file_name):
    with open(file_name,"r") as nun_text:
        new_num = nun_text.read()
        aaa = new_num.split(",")
        aaa = [int(x) for x in aaa]
        max_num = max(aaa)
        ful_numbers = list(range(0,max_num+1))
        the_miss_one = sum(ful_numbers) - sum(aaa)
        with open(r"found.txt", 'w') as found_num:
            found_num.write(str(the_miss_one))
        return the_miss_one








who_is_missing(r"C:\Users\Win10\Desktop\aaa.txt.txt")