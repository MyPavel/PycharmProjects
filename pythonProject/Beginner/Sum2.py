day = 14
month = 2
year = 2012
hours = 1
minutes = 3
seconds = 4
print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2

print("%02d:%02d:%02d" % (hours, minutes, seconds))