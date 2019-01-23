#----------------------------------------#
# Title: string_bits.py
# Initial File
# Claire Yoon,2019-01-21,New file
#----------------------------------------#

def string_bits(str):
  res = ''
  for i in range(len(str)):
    if i % 2 == 0:
      res = res + str[i]
  return res
