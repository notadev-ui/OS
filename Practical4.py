import os
import stat
import time
import sys

def file_details(file_name):
    try:
        stat_info = os.stat(file_name)
        permissions = stat.filemode(stat_info.st_mode)
        access_time = time.ctime(stat_info.st_atime)
        print(f"File: {file_name}")
        print(f"Owner Access Permissions: {permissions}")
        print(f"Last Access Time: {access_time}")
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")


file_details("practical4.py")