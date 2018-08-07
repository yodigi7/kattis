def get_avg_sl_min(num_cases: int):
    tot_sl_minute = 0
    tot_seconds = 0
    for _ in range(num_cases):
        sl_minute, seconds = input().split()
        tot_sl_minute += int(sl_minute)
        tot_seconds += int(seconds)
    avg = tot_seconds/float(tot_sl_minute*60)
    if avg <= 1:
        return "measurement error"
    return avg


if __name__ == '__main__':
    num_cases = int(input())
    print(get_avg_sl_min(num_cases))
