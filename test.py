
import os, re
import argparse
import codecs
import subprocess
import chardet
import functools

from PIL import Image
from pathlib2 import Path
from shutil import copyfile

with open("Data/README.md", 'rb') as f:
        s = f.read()
        chatest = chardet.detect(s)
        print s