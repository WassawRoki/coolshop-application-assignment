from datetime import datetime,timedelta,timezone
import holidays


    

def get_delivery_date(date : datetime):
    'From an input date finds the expected delivery date'
    
    '''This method is made such that a delivery can not happen in the weekend. 
    To add saturday delivery, simply remove the call to is_tomorrow_a_weekend_or_holiday()'''
    
    #dictionary of danish holidays
    dk_holidays = holidays.CountryHoliday('DK')
    
    #Add 2 extra buisness holidays
    dk_holidays['2021-12-31'] = "day before New years Eve"
    dk_holidays['2021-6-5'] = "Danish constetution day"
    
    #variable we keep updating till we find a delivery date
    expected_delivery_date : datetime = date
    temp_date : datetime = date
    
    #days to transport
    work_days : int =0
    

    days_since_order: int = 0
    
    while work_days < 2:
        #first we check if the date is not a weekend or a holiday
        if temp_date not in dk_holidays and temp_date.weekday() < 5 and is_tomorrow_a_weekend_or_holiday(dk_holidays, temp_date) == False:
            if temp_date.hour < 15:
                #as it was ordered before 15:00 the day counts as 2 buisness days
                work_days = work_days + 2
            else:
                work_days = work_days + 1
        elif temp_date not in dk_holidays and temp_date.weekday() < 5:
            work_days = work_days + 1
            
        #progress to the next day
        days_since_order = days_since_order + 1        
        temp_date = temp_date + timedelta(days=days_since_order)
        expected_delivery_date = expected_delivery_date + timedelta(days=1)

    return expected_delivery_date.strftime("%Y, %m, %d")

def is_tomorrow_a_weekend_or_holiday(holidays: dict, date: datetime):
    '''Method checks if tomorrow fromt he given date is a holiday or a weekend.'''
    tomorrow = date + timedelta(days=1)
    if tomorrow not in holidays and tomorrow.weekday() < 5:
        return False
    else:
        return True