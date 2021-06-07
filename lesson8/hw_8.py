from datetime import datetime

from collections import defaultdict


USERS = [
    {
        "name": "Bill",
        "birthday": datetime(year=1990, month=10, day=30).date()
    },
    {
        "name": "Andrew",
        "birthday": datetime(year=1990, month=11, day=2).date()
    },
    {
        "name": "Jill",
        "birthday": datetime(year=1989, month=11, day=30).date()
    },
    {
        "name": "Till",
        "birthday": datetime(year=1979, month=11, day=3).date()
    },
    {
        "name": "Jan",
        "birthday": datetime(year=1979, month=11, day=6).date()
    }]


def congratulate(USERS):
    cong_dict = defaultdict(list)
    for user in USERS:
        week_day = user["birthday"].replace(year=datetime.now().year).strftime('%A')
        if week_day == "Saturday" or week_day == "Sunday":
            week_day = "Monday"
        cong_dict[week_day].append(user["name"])
    for wekday, users in cong_dict.items():
        print_str = f"{wekday}:"
        for name in users:
            if name == users[-1]:
                print_str += f" {name}"
            else:
                print_str += f" {name},"
        print("\n" + print_str)    


def main():
    congratulate(USERS)
    
if __name__ == "__main__":
    main() 

