# date_and_time.py
import datetime
import	time	

myday = datetime.date(1995,1,22)
print(myday.day,myday.month, myday.year)

heute = datetime.date.today()
print(heute)

morgen = heute + datetime.timedelta(1)
print(morgen)

begin_ss = datetime.date(2019,3,1)
print("Der Semesterrest in Tagen:")
rest = begin_ss - heute
print(rest)

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond) #Systemzeit nicht Uhrzeit

print("Warte 5 sec")
time.sleep(5)
# Beim Aufruf von sleep() nimmt das Betriebssystem den Prozess aus der Menge der
# laufenden	Prozesse	heraus	und	steckt	ihn	in	eine	Warteschlange.	

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)