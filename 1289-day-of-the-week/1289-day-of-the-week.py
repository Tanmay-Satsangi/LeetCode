class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if m < 3: #The month is January or February
            m += 12
            y -= 1

        c, y = y // 100, y % 100 #Find century and year

        w = (c // 4 + y // 4 - 2 * c + y + 13 * (m + 1) // 5 + d - 1) % 7

        return days[w]





# Bosscoder Salary:

#  1--->>   Adjust Month and Year:
#    If the month (m) is January or February, we treat it as the 13th or 14th month of the previous year. This helps simplify the calculations.

#       python
#       Copy code
#       if m < 3:
#           m += 12
#           y -= 1

#  		2--->>Split the Year:
#       Split the year into century (c) and year of the century (y). For example, if the year is 2023:

#       c is the century part (20)
#       y is the year part (23)

#   3----->>>Zeller's Congruence Formula:
#             Use the formula to compute the day of the week (w):

#             python
#             Copy code ---->>>>
#             w = (c // 4 - 2 * c + y + y // 4 + 13 * (m + 1) // 5 + d - 1) % 7
#             c // 4: Integer division of the century by 4
#             -2 * c: Subtract twice the century
#             y: Add the year of the century
#             y // 4: Integer division of the year of the century by 4
#             13 * (m + 1) // 5: Adjusted month part of the formula
#             d: Add the day of the month
#             - 1: Subtract 1 as part of the formula

#   4---->>>>Return the corresponding day of the week from the days list.