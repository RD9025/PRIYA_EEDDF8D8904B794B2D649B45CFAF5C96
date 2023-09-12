#write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
year=int(input("Enter yearto be checked:
"))
if year %4==0:
    if year %100==0:
        if year %400==0:
           print ("The year is a leapyear!")
  else:
     print ("The year is not a leap year!")