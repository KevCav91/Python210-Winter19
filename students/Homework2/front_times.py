#----------------------------------------#
# Title: front_times.py
# Initial File
# Claire Yoon,2019-01-21,New file
#----------------------------------------#

def front_times(str, n):
  res = ''
  for i in range(n):
    res = res + str[:3]
  return res
