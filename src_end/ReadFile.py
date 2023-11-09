# Filesフォルダーの中身の全てのファイルのファイル名と行数を表示する

import os

def ReadFile():
    path = os.path.abspath(os.path.dirname(__file__)) + "/Files"
    files = os.listdir(path)
    for file in files:
        with open(path + "/" + file, "r") as f:
            print(file + " : " + str(len(f.readlines())) + "行")

ReadFile()