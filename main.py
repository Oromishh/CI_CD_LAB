import os
import argparse


arguments = argparse.ArgumentParser()
arguments.add_argument("-k", "--keyword", required=True, help="keyword to search for")

def get_arguments():
    try:
        return vars(arguments.parse_args())
    except:
        return {}

def get_keyword(arguments={}):
    return arguments.get("keyword", None)

def read_file(filename=None):
    content = None
    current_path = os.path.dirname(__file__)
    full_path = os.path.join(current_path, filename)
    try:
        with open(full_path) as file:
            content = file.read()
    except:
        content = None
    
    return content

def parse_lines(text = None):
    try:
        lines = text.split("\n")
        return lines
    except:
        return []
    
def filter_lines(lines=None, keywoard=""):
    content = []
    try:
        for line in lines:
            try:
                if keywoard in line:
                    content.append(line)
            except:
                pass
    except:
        pass

    return content

def save_lines(lines=None, filename=None):
    current_path = os.path.dirname(__file__)
    full_path = os.path.join(current_path, filename)
    try:
        text = "\n".join(lines)
        with open(full_path, mode="w") as file:
            file.write(text)
        return True
    except:
        return False

