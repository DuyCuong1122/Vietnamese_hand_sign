import os
import shutil

name_file = open(r'E:\hand\bone_name.txt', 'r')
data_name = name_file.read()
data_name_list = data_name.split('\n')

path_file = open(r'E:\hand\bone_path.txt', 'r')
data_path = path_file.read()
data_path_list = data_path.split('\n')

count = len(data_path_list)

for i in range(0, count):
    hand_path = os.path.join(data_path_list[i].replace('bone', 'image'), data_name_list[i])
    hand_path_new = os.path.join(data_path_list[i].replace('classes_bone', 'image'), data_name_list[i])
    #print(hand_path)
    #print(hand_path_new)
    try:
        shutil.move(hand_path, hand_path_new)
    except FileNotFoundError:
        pass
    text_name = data_name_list[i].replace('jpg', 'txt')
    point_path = os.path.join(data_path_list[i].replace('bone', 'point'), text_name)
    point_path_new = os.path.join(data_path_list[i].replace('classes_bone', 'point'), text_name)
    #print(point_path)
    #print(point_path_new)
    try:
        shutil.move(point_path, point_path_new)
    except FileNotFoundError:
        pass

    print(i)