'''2.	Write an if statement to determine whether a variable holding a year
 is a leap year. '''
leap_year = int(input('Enter any year:'))
if (leap_year % 4) == 0:
   if (leap_year % 100) == 0:
       if (leap_year % 400) == 0:
           print(f"{leap_year} is a leap year")
       else:
           print(f"{leap_year} is not a leap year")
   else:
       print(f"{leap_year} is a leap year")
else:
   print(f"{leap_year} is not a leap year")
