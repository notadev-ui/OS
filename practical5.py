import shutil

def copy_file(src, dest):
    try:
        shutil.copy2(src, dest)
        print(f"File copied from {src} to {dest}")
    except FileNotFoundError:
        print(f"Error: Source file {src} not found.")


copy_file('practical4.py', 'practical4Copy.py' )