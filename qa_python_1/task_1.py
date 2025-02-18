# Задание 1. Подсчёт количества минут.

data = '1h 45m,360s,25m,30m 120s,2h 60s'
result = 0
data_worked = data.split(',')
for time in data_worked:
    for t in time.split():
        if 'h' in t:
            t = t.replace('h', '')
            result += int(t) * 60
        elif 'm' in t:
            t = t.replace('m', '')
            result += int(t)
        elif 's' in t:
            t = t.replace('s', '')
            result += int(t) // 60

print(result)