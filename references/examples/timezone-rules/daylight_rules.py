from local_timezone import *

def first_sunday_on_or_after(when):
    days_to_go = 6 - when.weekday()
    if days_to_go:
        when += dt.timedelta(days_to_go)
    return when

DSTSTART_2007 = dt.datetime(1, 3, 8, 2)

DSTEND_2007 = dt.datetime(1, 11, 1, 2)

DSTSTART_1987_2006 = dt.datetime(1, 4, 1, 2)

DSTEND_1987_2006 = dt.datetime(1, 10, 25, 2)

DSTSTART_1967_1986 = dt.datetime(1, 4, 24, 2)

DSTEND_1967_1986 = DSTEND_1987_2006

def us_dst_range(year):
    # Find start and end times for US DST. For years before 1967, return
    # start = end for no DST.
    if 2006 < year:
        dststart, dstend = DSTSTART_2007, DSTEND_2007
    elif 1986 < year < 2007:
        dststart, dstend = DSTSTART_1987_2006, DSTEND_1987_2006
    elif 1966 < year < 1987:
        dststart, dstend = DSTSTART_1967_1986, DSTEND_1967_1986
    else:
        return (dt.datetime(year, 1, 1), ) * 2

    start = first_sunday_on_or_after(dststart.replace(year=year))
    end = first_sunday_on_or_after(dstend.replace(year=year))
    return start, end
