# 8:40 ~
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])

    terms_dict = {}
    for i in range(len(terms)):
        kind, date = terms[i].split()
        date = int(date)
        if date < 12:
            terms_dict[kind] = [0, date]
        else:
            terms_dict[kind] = [date//12, date%12]

    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        new_day = day
        new_year = year + terms_dict[kind][0]
        new_month = month + terms_dict[kind][1]
        if new_month > 12:
            new_year += (new_month//12)
            new_month = (new_month%12)

        if datetime(today_year, today_month, today_day) >= datetime(new_year, new_month, new_day):
            answer.append(i+1)
            
    return answer