# -------------------------- #
# Title: Warmup-1 > not_string
# Changelog:
# Russell Large, 1-16-19
# -------------------------- #


def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    add = "not"
    return add + ' ' + str
