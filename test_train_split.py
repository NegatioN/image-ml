import os
import random
import shutil

def make_folder(image_type):
    if not os.path.exists('{}/{}/{}'.format(output_path,image_type, "test")):
        os.makedirs('{}/{}/{}'.format(output_path,image_type, "test"))
    if not os.path.exists('{}/{}/{}'.format(output_path,image_type, "train")):
        os.makedirs('{}/{}/{}'.format(output_path,image_type, "train"))

def copy_files(image_type, test_or_train, file_list):
    for filename in file_list:
        shutil.copyfile('{}/{}/{}'.format(input_path, image_type, filename),
                        '{}/{}/{}/{}'.format(output_path, image_type, test_or_train, filename))
train_percent = 80

input_path = "output_ordered"
output_path = 'test_train'
output_types = filenames = os.listdir(input_path) #Needs fancy magic if data is not structured.

image_names_types = {}
for image_type in output_types:
    make_folder(image_type)
    image_names_types[image_type] = os.listdir('{}/{}'.format(input_path, image_type))
    random.shuffle(image_names_types[image_type])
print(image_names_types)

for image_type, image_list in image_names_types.items():
    print(image_list)
    train_num = int((len(image_list) / 100)*train_percent)
    train_files = image_list[:train_num]
    test_files = image_list[train_num:]
    copy_files(image_type, 'train', train_files)
    copy_files(image_type, 'test', test_files)