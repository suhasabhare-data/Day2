leap_year = {}
leap = False
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
       leap = True
    else:
       leap = False
    return leap
for i in range(1800,2100):
   print(i)
   print(is_leap(i))

   
def is_leap1(year):
    if year % 400 == 0 :
       leap = True
    else:
       leap = False
    return leap
for i in range(1800,2100):
   print(i)
   print(is_leap1(i))