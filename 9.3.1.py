def my_mp3_playlist(file_path):
    with open(file_path,'r') as file_dict:
        simple_txt = file_dict.read()
        aaa = simple_txt[1:].split('\n')
        cd_items =[]
        my_cd_dict = {}

        for line in aaa:
            cd_items.append(line.split(';'))

        for item in cd_items:
            my_cd_dict[item[0]] = (item[1], item[2])

        longest_song = None
        max_appearances = 0
        singer_appearances = {}

        for song, (singer, duration) in my_cd_dict.items():
            duration_minutes = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(':'))))

            if longest_song is None or duration_minutes > longest_song[1]:
                longest_song = (song, duration_minutes)

            if singer in singer_appearances:
                singer_appearances[singer] += 1
            else:
                singer_appearances[singer] = 1
    most_appeared_singer = max(singer_appearances, key=singer_appearances.get)

    return (
         longest_song[0],
         len(my_cd_dict),
         most_appeared_singer)




print(my_mp3_playlist(r'C:\Users\Win10\Desktop\aaa.txt.txt'))






#
# """Displays info of playlist, read from a file: the longest song, number of songs in list, the most frequent singer
# :param: file_path: th path to playkust file
# :type: string
# :return: info about the playlist
# :rtype: tuple
# """
# def my_mp3_playlist(file_path):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	song_lengths, artist_count = {}, {}
# 	length = len(lines)
# 	for line in lines:
# 		line_list = line.split(';')
# 		song_lengths[line_list[0]] = line_list[2]
# 		if line_list[1] in artist_count.keys():
# 			artist_count[line_list[1]] = artist_count[line_list[1]] + 1
# 		else:
# 			artist_count[line_list[1]] = 1
# 	return max(song_lengths, key=song_lengths.get), length, max(artist_count, key=artist_count.get)