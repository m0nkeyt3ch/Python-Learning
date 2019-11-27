#function to judge the year is leapyear or not
def leapyear(y):
	return (y%400 == 0 or (y % 4 == 0 and y % 100 == 0))

days = [0,31,28,31,30,31,30,31,31,30,31,30]
res = 0

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

if leapyear(year):
	days[2] += 1

for i in range(month):
	res += days[i]

print(f"Year {year} Day {res+day}")
