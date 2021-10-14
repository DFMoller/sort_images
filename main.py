from PIL import Image
from PIL.ExifTags import TAGS
import os

directory = "Germany 2021"
for count, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".JPG"):
        exifdata = Image.open(directory + "/" + filename).getexif()
        if count == 0:
            print(exifdata)
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes 
                if isinstance(data, bytes):
                    data = data.decode()
                print(f"{tag:25}: {data}")
                # print(tag)