# def my_mp4_playlist(file_path, new_song):
#     # Read the existing content from the file
#     with open(file_path,'r') as file:
#         lines = file.readlines()
#
#     # Check if there are at least three lines in the file
#     if len(lines) < 3:
#         # Add empty lines to reach the third line
#         lines.extend(['\n'] * (3 - len(lines)))
#
#     # Update the third line with the new song
#     lines[4] = "{aaa};Unknown;4:15;\n".format(aaa = new_song)
#
#     # Write the updated content back to the file
#     with open(file_path, 'w') as file:
#         file.writelines(lines)
#
#     # Print the updated content
#     with open(file_path, 'r') as file:
#        return (file.read())
#
# print(my_mp4_playlist(r'C:\Users\Win10\Desktop\aaa.txt.txt',"Python Love Story"))

def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as file:
        songs = file.readlines()
        if len(songs) >= 3:
            songs[2] = new_song + songs[2][songs[2].find(';'):]
        else:
            songs.append('\n' *  (2 - len(songs)))
            songs.append(new_song + ';')

        for song in songs:
            print(song, end='')
        # text = ''
        # for i in range(len(songs)):
        #     text=text+songs[i]
        # print(songs)


my_mp4_playlist(r'C:\Users\Win10\Desktop\aaa.txt.txt',"hello")



# def my_mp4_playlist(file_path, new_song):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	if len(lines) >= 3:
# 		lines[2] = new_song + lines[2][lines[2].find(';'):]
# 		#open(file_path, "w").writelines(lines)
# 	else:
# 		for n in range(2 - len(lines)):
# 			lines.append("\n")
# 		lines.append(new_song+ ";")
# 		#open(file_path, "w").writelines(lines)
# 	#print(open(file_path, "r").read())
# 	text=''
# 	for i in range(len(lines)):
# 		text=text+lines[i]
# 	print(text)


