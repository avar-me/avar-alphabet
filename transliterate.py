#!/usr/bin/env python3

from dicts import latin2_dict, ajam_dict, \
                  latin_dict, latin_conv_dict, check_req_dict


# currently only smallcase letters are supported. Need to rework this.
def lowp(string):
    return string.lower().replace("і", "І")


def cyr2latin(string):
    string = lowp(string)
    if string[0] == "е":
        string = "й" + string   # some dirty code
    for k, v in latin2_dict:
        string = string.replace(k, v)
    return string


def cyr2ajam(string):
    string = lowp(string)
    if string[0] in ["и", "у", "о"]:
        string = "ъ" + string
    if string[0] == "э":
        string = "ъе" + string[1:]
    for k, v in ajam_dict:
        string = string.replace(k, v)
    return string


def cyr2latin0(string):
    string = cyr2ajam(string)
    for k, v in latin_dict:
        string = string.replace(k, v)
    return string


def latin2latin(string):
    if string[0] == "e":
        string = "y"+string
    if string[0:2] == "'o":
        string = string[1:]
    if string[0:2] == "'i":
        string = string[1:]
    if string[0:2] == "'u":
        string = string[1:]
    for k, v in latin_conv_dict:
        string = string.replace(k, v)
    return string


def normalize_request(string):
    # only words, no sentences support
    string = string.strip().split(" ")[0]
    # need to rework this step. Currently all letters are treated as small-case
    string = string.lower()
    # every incorrect "palochka" should be replaced with correct
    # WARNING 1, !
    for k, v in check_req_dict:
        string = string.replace(k, v)
    return string


if __name__ == '__main__':
    import sys
    import fileinput
    nr = normalize_request
    for line in fileinput.input():
        line = line.rstrip()
        line = nr(line)
        print(f'{line}:{cyr2latin0(line)}:{cyr2ajam(line)}:{cyr2latin(line)}')
