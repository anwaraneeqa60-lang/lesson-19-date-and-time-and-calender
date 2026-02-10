import random
import time
def getrandomdate(stardate, enddate):
    print("printing random date between", stardate , "and", enddate)
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(stardate , dateformat))
    endtime = time.mktime(time.strptime(enddate , dateformat))
    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("random date =", getrandomdate("1/1/2020", "12/12/2018"))