from bs4 import BeautifulSoup
import os
import shutil

output_dir = "output_ordered"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def imagenet_to_theano_format(filename):
    with open(filename) as xml_file:
        soup = BeautifulSoup(xml_file, "lxml")
        annotation = soup.html.body.annotation
        image_path = annotation.path.text
        label = annotation.object.find('name').text
        if not os.path.exists('{}/{}'.format(output_dir,label)):
            os.makedirs('{}/{}'.format(output_dir,label))
        shutil.copyfile(image_path, '{}/{}/{}.{}'.format(output_dir, label, annotation.filename.text, "jpg"))

path = "."
filenames = os.listdir(path)

for filename in filenames:
    if ".xml" in filename:
        print(filename)
        imagenet_to_theano_format('{}/{}'.format(path, filename))


#TODO do some sort of crop of the image?
#TODO add negative examples? all imgs which dont have an xml.
