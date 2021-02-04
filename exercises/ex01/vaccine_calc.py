"""A vaccination calculator."""

__author__ = "730333306"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
dpd: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))
answer: int = int(((population * 2 * (target/100)) - doses) / dpd)
today: datetime = datetime.today()
time_addition: timedelta = timedelta(answer)
target_date: datetime = today + time_addition
print("We will reach " + str(target) + "% vaccination in " + str(answer) + " days, which falls on " + str(target_date.strftime("%B %d, %Y")))