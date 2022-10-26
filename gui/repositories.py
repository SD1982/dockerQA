"""
"""

import subprocess


global HTML_FOLDER_PATH

HTML_FOLDER_PATH = '../html/'


def clone_branch(branch):
    match branch:
        case "develop":
            command = 'echo clone develop'
        case "1.7.8.x":
            command = 'echo clone 1.7.8.x'
        case "8.0.x":
            command = 'echo clone 8.0.x'
    subprocess.run(['bash', '-c', command], shell=False, cwd=HTML_FOLDER_PATH)


def update_branch(branch):
    match branch:
        case "develop":
            command = 'echo update develop'
        case "1.7.8.x":
            command = 'echo update 1.7.8.x'
        case "8.0.x":
            command = 'echo update 8.0.x'
    subprocess.run(['bash', '-c', command], shell=False, cwd=HTML_FOLDER_PATH)


def remove_branch(branch):
    match branch:
        case "develop":
            command = 'echo remove develop'
        case "1.7.8.x":
            command = 'echo remove 1.7.8.x'
        case "8.0.x":
            command = 'echo remove 8.0.x'
    subprocess.run(['bash', '-c', command], shell=False, cwd=HTML_FOLDER_PATH)