import os
import shutil

TARGET = '1. target'
SELECTED = '3. selected'
ORIGINAL = '4. original'

for root, dirs, files in os.walk(SELECTED):
    for f in files:
        extension = os.path.splitext(f)[1]
        # print(extension)
        if extension == '.JPG':

            subdir = os.path.split(root)[1]
            selected_subdir = os.path.join(SELECTED, subdir)
            target_subdir = os.path.join(TARGET, subdir)
            original_subdir = os.path.join(ORIGINAL, subdir)
            
            if not os.path.exists(original_subdir):
                os.mkdir(original_subdir)
            
            src = os.path.join(target_subdir, f)
            dst = os.path.join(original_subdir, f)
            print(src, ">>>", dst)

            shutil.copyfile(src, dst)