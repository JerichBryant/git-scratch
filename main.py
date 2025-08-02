import os
import sys
import json
import time
import argparse
import shutil
import pathlib

#everything is asssumption literally have no clue
def Node():
    pass

def Tree():
    # each directory gets a node and then to commit it takes the current tree uses bfs to get structure and add tree object to dictionary paired with a message
    def Tree(self):
        pass

    def bfs():
        # create empty set to track visited nodes
        # create empty queue and empty array
        # once node is visited dequeue and add node to array
        # check enqueue neighbors
        # then dequee and iterate full until end of tree
        pass
    def dfs():
        # create a empty set to track visited nodes
        # if root is null return the root
        # use recursion to get to bottom of the tree and push and pop stack based on iteration
        # then add to array as needed 
        pass
    
def LinkedList():
    # store commits in linked list
    # head = most recent commit
    pass

def sha1_algorithm():
    pass

def git_init():
    dir_name = ".mygit/"
    try:
        os.mkdir(dir_name)
        print("git initialized")
    except FileExistsError:
        print("file exists")
    except Exception as e:
        print(f"error: {e}")


def commit():
    # takes the objects hashed(blob) from the .mygit and inserts into a tree structure in mygit linked with a message timestamp
    # stores into the mygit file update the latest commit name to head 
    pass

def git_message():
    #map a message to the commit
    pass

def hash_file(file):
    #takes file and hashes it using sha-1 algorithm with the hashlib library
    pass


def git_add(file):
    #adds hashed file stores into the .mygit
    # create a dictionary to match the blob
    pass

def git_remove(file):
    #removes file index from .mygit
    pass

def git_log():
    # print out the head commit in the git file
    pass
if __name__ == "__main__":
    #run program in here
    pass
