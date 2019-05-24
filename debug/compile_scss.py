import sass
import os

SASS_DIR = "../assets/scss"

def is_scss(path):
    return path[-5:] == ".scss"

def get_file_text(path):
    result = ""
    with open(path) as f:
        result = f.read()
    return result

def compile_scss(path, file):
    scss = get_file_text(path)
    help(sass)
    print(sass.compile(scss))
    

for root, dirs, files in os.walk(SASS_DIR):
    for file in files:
        path = os.path.join(root, file)
        print(path)
        if is_scss(path):
            compile_scss(path, file)
