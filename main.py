def sum_timetamps(timestamps):

    total_second = 0
    for timestamp in timestamps:
        minutes, seconds = map(int, timestamp.split(':'))
        total_second += minutes * 60 + seconds

    minutes = total_second // 60
    seconds = total_second % 60

    return f'{minutes}:{seconds}'


timestamps = ['04:20', '03:35', '02:00']
total_time = sum_timetamps(timestamps)
print(total_time)
