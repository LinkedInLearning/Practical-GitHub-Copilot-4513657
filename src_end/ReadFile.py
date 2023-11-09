# Filesフォルダーの中身の全てのファイルのファイル名と行数を表示する

import os

def ReadFile():
    path = os.path.abspath(os.path.dirname(__file__)) + "/Files"
    files = os.listdir(path)
    for file in files:
        with open(path + "/" + file, "r") as f:
            print(file + " : " + str(len(f.readlines())) + "行")

ReadFile()

# 足し算を行う関数を作成する
def add_numbers(num1, num2):
    return num1 + num2