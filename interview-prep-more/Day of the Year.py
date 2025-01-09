"""
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29

        day_number = sum(days_in_month[:month - 1]) + day
        return day_number
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        list_year=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        day=int(date[-2:])
        year=int(date[:4])
        month=int(date[5:7])

        if year%4==0 and year!=1900 and month>2 :
            day+=1
        
        return list_year[month-1]+day
