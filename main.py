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
