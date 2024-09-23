from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        days_difference = (given_date - today).days           
    except ValueError as e:
        print('Error: The date format must be: "YYYY-MM-DD"')
    else:
        print(days_difference)
            
get_days_from_today("2024-02-05")
get_days_from_today("2025-02-05")
get_days_from_today("2025.02.05")
get_days_from_today("aaff/nh/jj")
