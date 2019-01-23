#----------------------------------------#
# Title: string_splosion.py
# Initial File
# Claire Yoon,2019-01-21,New file
#----------------------------------------#


def string_splosion(str):
    res = ''
    for i in range(len(str)):
        for j in range(i + 1):
            res = res + str[j]

    return res
