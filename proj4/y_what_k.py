# Lauren Trinks March 20

# This program uses the quirks of the gregorian calendar and unix time systems to determine on what month and year
# a Unix system with a given number of bits will rollover and crash

#https://en.wikipedia.org/wiki/Gregorian_calendar
#https://en.wikipedia.org/wiki/Unix_time

# say the prompt and get the number of bits the computer will have
print("When will your theoretical (or real) computer break due to time? Answer this to find out!")
bits = int(input("How many bits does this computer use to store time? "))

# find the maximum value that can be stored in a signed int with the given number of bits
maxValue = pow(2, bits - 1) - 1

# max value is the number of seconds past 00:00:00 Jan 1 1970 that the computer will break
# use the gregorian calendar laws to figure out what date and year this is

# get starting units of time, these only have one
secondLength = 1
minuteLength = 60 * secondLength
hourLength = 60 * minuteLength
dayLength = 24 * hourLength

# there are 4 possible lengths for a month
month30Length = 30 * dayLength
month31Length = 31 * dayLength
month28Length = 28 * dayLength
month29Length = 29 * dayLength

# there are 2 possible year lengths
yearLength = 7 * month31Length + 4 * month30Length + month28Length
leapYearLength = yearLength + dayLength

# figure out what year the computer will crash using the gregorian calendar rules

# there will be a leap year if the year is divisible by 4
# if the year is divisible by 4 and 100 it will not be a leap year
# if the year is divisible by 4 and 400 it will be a leap year

startYear = 1970
curYear = startYear

secLeft = maxValue
prevSecLeft = -1

while secLeft > 0:
    prevSecLeft = secLeft
    # loops every 400 years, compute how many times there are 400 year loops to save TONS of time
    if secLeft - (97 * leapYearLength + 303 * yearLength) > 0:
        curYear = curYear + 400 * int(secLeft / (97 * leapYearLength + 303 * yearLength))
        secLeft = secLeft % (97 * leapYearLength + 303 * yearLength)
    else:
        if curYear % 4 == 0:
            if curYear % 400 == 0:
                secLeft = secLeft - leapYearLength
                curYear = curYear + 1
            if curYear % 100 == 0:
                secLeft = secLeft - yearLength
                curYear = curYear + 1
            else:
                secLeft = secLeft - leapYearLength
                curYear = curYear + 1

        else:
            secLeft = secLeft - yearLength
            curYear = curYear + 1

secLeft = prevSecLeft
breakYear = curYear - 1

# Figure out what month the computer will break, this is really messy I know

breakMonth = "January"

if secLeft > month31Length:
    breakMonth = "February"
    secLeft = secLeft - month31Length

if curYear % 4 == 0:
    if curYear % 100 == 0:
        if curYear % 400:
            if secLeft > month29Length:
                breakMonth = "March"
                secLeft = secLeft - month29Length
        if secLeft > month28Length:
            breakMonth = "March"
            secLeft = secLeft - month28Length
    if secLeft > month29Length:
        breakMonth = "March"
        secLeft = secLeft - month29Length
else:
    if secLeft > month28Length:
        breakMonth = "March"
        secLeft = secLeft - month28Length

if secLeft > month31Length:
    breakMonth = "April"
    secLeft = secLeft - month31Length

if secLeft > month30Length:
    breakMonth = "May"
    secLeft = secLeft - month30Length

if secLeft > month31Length:
    breakMonth = "June"
    secLeft = secLeft - month31Length

if secLeft > month30Length:
    breakMonth = "July"
    secLeft = secLeft - month30Length

if secLeft > month31Length:
    breakMonth = "August"
    secLeft = secLeft - month31Length

if secLeft > month31Length:
    breakMonth = "September"
    secLeft = secLeft - month31Length

if secLeft > month30Length:
    breakMonth = "October"
    secLeft = secLeft - month30Length

if secLeft > month31Length:
    breakMonth = "November"
    secLeft = secLeft - month31Length

if secLeft > month31Length:
    breakMonth = "December"
    secLeft = secLeft - month31Length

print("Your computer will break in " + breakMonth + " of the year " + str(breakYear))
