def month_to_season(n_month):
    if n_month in (12,1,2):
        return "зима"
    if n_month in (3,4,5):
        return "весна"
    if n_month in (6,7,8):
        return "наконец-то лето!"
    if n_month in (9,10,11):
        return "опять осень"
    else:
        return "некорректный ввод"


n_month = int(input("Введите номер месяца: "))
season = month_to_season(n_month)
print(season)