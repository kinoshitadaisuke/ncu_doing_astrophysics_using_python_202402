#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/17 12:10:32 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing pathlib module
import pathlib

# importing pillow module
import PIL.Image

# directory for storing cropped PNG files
dir_cropped = 'iss3d_cropped'

# making a pathlib object for the directory
path_dir_cropped = pathlib.Path (dir_cropped)

# if the directory does not exist, then create it
if not (path_dir_cropped.exists ()):
    path_dir_cropped.mkdir (mode=0o755)

# making a pathlib object for currently working directory
path_pwd = pathlib.Path ('.')

# obtaining a list of PNG files in the directory "iss3d"
list_original = path_pwd.glob ('iss3d/*.png')

# processing each PNG file
for file_original in sorted (list_original):
    # making a pathlib object for original PNG file
    path_original = pathlib.Path (file_original)
    # cropped PNG file
    file_cropped = dir_cropped + '/' + path_original.stem + 'c.png'
    # making a pathlib object for cropped PNG file
    path_cropped = pathlib.Path (file_cropped)
    print (f'{path_original} ==> {path_cropped}')

    # opening image file using pillow
    with PIL.Image.open (path_original) as image_original:
        # region for cropping
        region = [768, 432, 2688, 1512]

        # cropping image
        image_cropped = image_original.crop (region)

        # saving image into a file
        image_cropped.save (path_cropped)
