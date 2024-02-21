def add_time(time,add,week = None):
    actual_time = []
    actual_time2 = [actual_time.append(i) for i in time]

    time_zone = [str(i)+'M' for i in time if i == "P" or i == "A"]

    next_time = []
    next_time2 = [next_time.append(i) for i in add]

    def get_time(subject):

        numbers = [int(i) for i in subject if i.isdigit()]
        numbers = [str(i) for i in numbers]

        hours = ""
        minutes = ""
        minutes_total = 0

        if len(numbers) > 4:
            for i in range(len(numbers)):
                if i == len(numbers)-1 or i == len(numbers)-2:
                    minutes += numbers[i]
                else:
                    hours += numbers[i]

        elif len(numbers) == 4:
            for i in range(4):
                if i <= 1:
                    hours += numbers[i]
                else:
                    minutes += numbers[i]
        else:
            for i in range(3):
                if i == 0:
                    hours += numbers[i]
                else:
                    minutes += numbers[i]

        hours = int(hours)
        minutes = int(minutes)
        minutes_total = (hours*60)+minutes

        return minutes_total

    def get_new_time(week = None):

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        actual_time_minutes = get_time(actual_time)
        next_time_minutes = get_time(next_time)

        next_time_minutes = actual_time_minutes+next_time_minutes
        hour = int(next_time_minutes/60)
        minutes = (next_time_minutes % 60)

        if week != None:
            week = week.lower()
            if week == 'monday':
                days_count = 0
            elif week == 'tuesday':
                days_count = 1
            elif week == 'wednesday':
                days_count = 2
            elif week == 'thursday':
                days_count = 3
            elif week == 'friday':
                days_count = 4
            elif week == 'saturday':
                days_count = 5
            elif week == 'sunday':
                days_count = 6
        else:
            days_count = 0

        counter = 0

        while hour >= 12:
            if time_zone[0] == "PM":
                days_count += 1
                counter+=1
                time_zone[0] = "AM"
            elif time_zone[0] == "AM":
                time_zone[0] = 'PM'
            if days_count == 7:
                days_count = 0
            if hour == 12:
                break
            hour -= 12

        hour = str(hour)
        minutes = str(minutes)

        if counter == 0:
            last_event = ""
        elif counter == 1:
            last_event = " (next day)"
        else:
            last_event = f" ({counter} days later)"

        if len(minutes) == 1:
            minutes = "0"+minutes


        if week == None:
            string_final = hour+":"+minutes+" "+time_zone[0]+last_event
            return string_final
        else:
            string_final = hour+":"+minutes+" "+time_zone[0]+", "+days[days_count]+last_event
            return string_final

    return get_new_time(week)
