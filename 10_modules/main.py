# without alias
# import report
#
# description = report.getDescription()
# print("Today's weather:", description)

# with alias
# import report as wr # alias is not mandatory
#
# description = wr.getDescription()
# print("Today's weather:", description)

# only part of the module
# from report import getDescription
#
# description = getDescription()
# print("Today's weather:", description)

# only part of the module with alias
from report import getDescription as doIt

description = doIt()
print("Today's weather:", description)


# module search path
import sys
for place in sys.path:
    print(place)
