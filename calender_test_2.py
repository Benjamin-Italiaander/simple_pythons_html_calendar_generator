# import module
import calendar
import xml.etree.ElementTree as etree
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')
YEAR = int(input("Enter Year: "))
startMONTH = int(input('Enter start month: '))
endMONTH = int(input("Enter end month: "))


print(open('header.txt', 'r').read())
#print("</caption><thead>")
    
for x in range((startMONTH), (endMONTH)):
    htmlStr = '<br><br><main><table class="calendar">'
    #htmlStr = ("<h1>",(YEAR),"</h1></caption><thead>")
    htmlStr = htmlStr.replace("</thread>","")
    myCal = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlStr = (str(htmlStr) + myCal.formatmonth(YEAR, x))
    htmlStr = htmlStr.replace("th class=",'th class="calendar__day__header')
    htmlStr = htmlStr.replace("&nbsp;","")
    htmlStr = htmlStr.replace("</table>","</table></thead></main><br><br><br><br><br>")
    htmlStr = htmlStr.replace("td class=",'td class="calendar__day__cell')
    htmlStr = htmlStr.replace('<table border="0" cellpadding="0" cellspacing="0" class="month">',"")
    #htmlStr = (str(htmlStr) + ('</table></thead><br><br><br>'))
    print (htmlStr)

    
print(open('footer.txt', 'r').read())




