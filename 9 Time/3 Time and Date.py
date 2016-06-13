from time import localtime, strftime
datetime = strftime("%A (%a), %d %b %Y %H:%M:%S", localtime())
print(datetime)
