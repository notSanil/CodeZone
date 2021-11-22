import datetime

user = {}

def new_data(username, year, month, date, xp):
    global user
    user[username] = []
    user[username].append([datetime.date(year, month, date)])
    user[username].append([xp])

def append_data(day, username, xp):
    global user

    first_date = user[username][0][0]
    today = first_date + datetime.timedelta(days = day)
    user[username][0].append(today)
    user[username][1].append(xp)
    
# new_data('a', 2021, 9, 21, 500)
# append_data(1, 'a', 1000)
# print(user)