import os
import re

def main():
    txt_dir = "/home/chenyifan/Datasets_3/Magicdata_750h/train/TRANS.txt"

    text_writter_train = open("text_train", "a+")

    txt_reader = open(txt_dir)
    txt_all = txt_reader.readlines()

    for line in txt_all:
        splited_str = line.split("\t", 3)
        text_line = splited_str[0] + ' ' + splited_str[2]
        text_writter_train.writelines(text_line)

    return 0

if __name__ == "__main__":
    main()