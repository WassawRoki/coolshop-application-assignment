from datetime import datetime,timedelta,timezone
import holidays

def get_delivery_date(date : datetime):
    'From an input date finds the expected delivery date'
    
    #dictionary of danish holidays
    dk_holidays = holidays.country_holidays('DK')
    
    expected_delivery_date : datetime = date
    temp_date : datetime = date
    
    work_days : int =0
    #we want to add 2 workdays to the delivery time.
    days_since_order: int = 0
    
    
    while work_days < 2:
        #first we check if the date is not a weekend or a holiday
        temp_date = date + timedelta(days=days_since_order+1)
        if temp_date.hour < 15:
            if temp_date not in dk_holidays and temp_date.weekday() < 5:
                days_since_order +=1
                expected_delivery_date += timedelta(days=1)
                work_days = work_days+2
            else:
                expected_delivery_date += timedelta(days=1)
                days_since_order +=1
        else:
            if temp_date not in dk_holidays and temp_date.weekday() < 5:
                days_since_order +=1
                work_days = work_days+1
            else:
                days_since_order +=1


    
    return expected_delivery_date.strftime("%Y, %m, %d")

get_delivery_date(datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc))