def add_time(start, duration, day=None):
    # Parse start time
    time_part, period = start.split()
    start_h, start_m = map(int, time_part.split(':'))
    
    # Convert to 24-hour format
    if period == 'PM' and start_h != 12:
        start_h += 12
    elif period == 'AM' and start_h == 12:
        start_h = 0

    # Parse duration
    dur_h, dur_m = map(int, duration.split(':'))
    
    # Add minutes
    new_m = start_m + dur_m
    carry_h = new_m // 60
    new_m %= 60
    new_m = f"{new_m:02d}"  # Ensure two digits

    # Add hours
    new_h = start_h + dur_h + carry_h
    carry_d = new_h // 24
    new_h %= 24

    # Determine AM/PM
    if new_h >= 12:
        period = 'PM'
        if new_h > 12:
            new_h -= 12
    else:
        period = 'AM'
        if new_h == 0:
            new_h = 12

    # Handle day of the week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_str = ''
    if day:
        day_idx = (days.index(day.lower()) + carry_d) % 7
        day_str = ', ' + days[day_idx].capitalize()

    # Handle days later annotation
    days_later = ''
    if carry_d == 1:
        days_later = ' (next day)'
    elif carry_d > 1:
        days_later = f' ({carry_d} days later)'

    return f"{new_h}:{new_m} {period}{day_str}{days_later}"
