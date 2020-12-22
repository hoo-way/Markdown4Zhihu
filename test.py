
import os, re
import argparse
import codecs
import subprocess
import chardet
import functools

from PIL import Image
from pathlib2 import Path
from shutil import copyfile


def rename_image_ref(m, original=True):
    global image_folder_path
    print(Path(m.group(2)))
    # if not Path(m.group(2)).is_file():
    #     print("e1")
    #     return m.group(0)
    if os.path.getsize(image_folder_path.parent/m.group(1+int(original)))>COMPRESS_THRESHOLD:
        if original:
            print("e2")
            image_ref_name = Path(m.group(2)).stem+".jpg"
        else:
            print("e3")
            image_ref_name = Path(m.group(1)).stem+".jpg"
    else:
        if original:
            print("e4")
            image_ref_name = Path(m.group(2)).name
        else:
            print("e5")
            image_ref_name = Path(m.group(1)).name
    if original:
        print("e6")
        return "!["+m.group(1)+"]("+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+image_ref_name+")"
    else:
        print("e7")
        return '<img src="'+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/" +image_ref_name +'"'

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')
    args = parser.parse_args()
    args.input = Path("Data\README.md")
    image_folder_path = args.input.parent/(args.input.stem)
    print(image_folder_path)

    with open("Data\README.md", 'rb') as f:
        s = f.read()
        chatest = chardet.detect(s)
        # print(chatest)
        
    with open(str(args.input),"r",encoding=chatest["encoding"]) as f:
        lines = f.read()
        _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)",functools.partial(rename_image_ref, original=True), lines)
        # print(str(functools.partial(rename_image_ref, original=True)))
        # matchObj = (re.search(r"\!\[(.*?)\]\((.*?)\)", lines)) 
        # print(matchObj)
        _lines = re.sub('(\$)(?!\$)(.*?)(\$)', ' <img src="https://www.zhihu.com/equation?tex=\\2" alt="\\2" class="ee_img tr_noresize" eeimg="1"> ', _lines)
        # print(_lines)
        