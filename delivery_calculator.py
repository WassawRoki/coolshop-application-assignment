from datetime import datetime,timedelta
import holidays

def get_delivery_date(date : datetime):
    
    #dictionary of danish holidays
    dk_holidays = holidays.country_holidays('DK')
    
    expected_delivery_date : datetime = date
    current_datetime = datetime.now()
    
    days_added : int = 0
    tempdays = 0
    #we want to add 2 workdays to the delivery time.
    while days_added < 2:
        tempdays = tempdays + timedelta(days=1)
        #first we check if the date is not a weekend or a holiday
        if date.hour < 15:
            if date + timedelta(days=1)+tempdays not in dk_holidays and (date + timedelta(days=1)+tempdays).weekday() < 5:
                days_added +=2
                expected_delivery_date += timedelta(days=1)
            else:
                expected_delivery_date += timedelta(days=1)
        else:
            if date + timedelta(days=1) + expected_delivery_date not in dk_holidays and (date + timedelta(days=1)+ expected_delivery_date).weekday() < 5:
                days_added +=1
                expected_delivery_date += timedelta(days=1)
            else:
                expected_delivery_date += timedelta(days=1)
        
    
    return expected_delivery_date.strftime("%Y, %m, %d")