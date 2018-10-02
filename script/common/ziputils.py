#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time,  datetime 

def zipDir(dir_path,file_zip):   

    zipf = zipfile.ZipFile(file_zip, "w",zipfile.ZIP_DEFLATED)
    # 压缩目录
    pre_len = len(os.path.dirname(dir_path))
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
 
    zipf.close()  


def un_zip(file_zip,out_dir):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_zip)
    if os.path.isdir(out_dir):
        pass
    else:
        os.mkdir(out_dir)
    for names in zip_file.namelist():
        zip_file.extract(names,out_dir)
    zip_file.close()


