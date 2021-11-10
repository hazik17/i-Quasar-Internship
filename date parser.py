from datetime import datetime
date1='june 8, 2011'
date2='08/10/29'
date3='09-30-1999 12:23:03'
date1_obj =datetime.strptime(date1, '%B %d, %Y')
print(date1_obj)
