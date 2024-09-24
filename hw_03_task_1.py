from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        days_difference = ((given_date - today).days) + 1  
        return days_difference       
    except ValueError as e:
        return 'Error: The date format must be: "YYYY-MM-DD"' 
  
            
print(get_days_from_today("2024-09-22"))
print(get_days_from_today("2024-09-24"))
print(get_days_from_today("2024-09-23"))
print(get_days_from_today("2025.02.05"))
print(get_days_from_today("aaff/nh/jj"))