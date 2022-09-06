
# import module
import calendar
import xml.etree.ElementTree as etree
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')

MONTH = 9
YEAR = 2022
#print file with python
print(open('header.txt', 'r').read())
#print(calendar.month_name(month))

Maandnaam=(calendar.month_name[MONTH])

print("<h1>",(Maandnaam),(YEAR),"</h1>")
print("</caption><thead>")

myCal = calendar.HTMLCalendar(calendar.SUNDAY)
htmlStr = myCal.formatmonth(YEAR, MONTH)
htmlStr = htmlStr.replace("th class=",'th class="calendar__day__header')
htmlStr = htmlStr.replace("&nbsp;","")
htmlStr = htmlStr.replace("td class=",'td class="calendar__day__cell')
htmlStr = htmlStr.replace('<table border="0" cellpadding="0" cellspacing="0" class="month">',"")


#root = etree.fromstring(htmlStr)
#for elem in root.findall("*//td"):
#    if elem.get("class") != "tue":
#        continue
#    elem.text += "!"

#    br = etree.SubElement(elem, "br")
#    br.tail = "cool!"

print (htmlStr)
print(open('footer.txt', 'r').read())




### calender in html formaat
#hc = calendar.HTMLCalendar(calendar.THURSDAY)
#str = hc.formatmonth(2022, 8)
#print(str)

#for day in calendar.day_name:
#    print(day)

#for day in calendar.day_number:
#    print(day)


#mycal = calendar.monthcalendar(2025, 9)
# The first MONDAY has to be within the first two weeks
#        week1 = mycal[0]
#        week2 = mycal[1]


    
#print ("De eerste maandag van de maand augustus")
#mycal = calendar.monthcalendar(2022, 9)
 #   week1 =(mycal[0])
 #   week2 = mycal
    
#print(week2)   

#print(mycal)    

#print(week1) 

# display the calendar
# print(calendar.month(yy, mm))


#print ("The calendar of year 2018 is : ")
#print (calendar.calendar(2018, 2, 1, 6))
