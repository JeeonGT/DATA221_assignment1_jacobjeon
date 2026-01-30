#3600 seconds in an hour
#60 seconds in a minute

def seconds_time_conversion(seconds_since_midnight):
    seconds_left = 0
    if 43200 >= seconds_since_midnight >= 0:

        if seconds_since_midnight >= 3600:
            hours = seconds_since_midnight // 3600
            seconds_left = seconds_since_midnight - (hours * 3600)
        else:
            hours = 0
            seconds_left = seconds_since_midnight


        if seconds_left >= 60:
            minutes = seconds_left // 60
            seconds_left = seconds_left - (minutes * 60)
        else:
            minutes = 0
        print(f"The time is {hours}h {minutes}m {seconds_left}s AM.")



    elif 86400 >= seconds_since_midnight > 43200:
        if seconds_since_midnight >= 3600:
            hours = seconds_since_midnight // 3600
            seconds_left = seconds_since_midnight - (hours * 3600)
            hours = hours - 12
        else:
            hours = 0
            seconds_left = seconds_since_midnight


        if seconds_left >= 60:
            minutes = seconds_left // 60
            seconds_left = seconds_left - (minutes * 60)
        else:
            minutes = 0
        print(f"The time is {hours}h {minutes}m {seconds_left}s PM.")
    else:
        print(f"The time is %^*%*&h @%%$#m _)$**^&s AM.")
        print("You've gone too far! More than a whole day has passed. Wake up")

seconds_time_conversion(86407)


