"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
"""

class Solution():
    def format_duration(self, seconds):
        retstr = ""
        if seconds == 0:
            return "now"
        lst = [0 for _ in range(5)]
        minutes = seconds // 60
        seconds = seconds % 60

        hours = minutes // 60
        minutes = minutes % 60

        days = hours // 24
        hours = hours % 24

        years = days // 365
        days = days % 365

        lst[0] = years
        lst[1] = days
        lst[2] = hours
        lst[3] = minutes
        lst[4] = seconds

        count = sum([1 for x in lst if x > 0])

        if years > 0:
            retstr += str(years)
            retstr += " years" if years > 1 else " year"
            if count == 2:
                retstr += " and "
            elif days > 0 or hours > 0 or minutes > 0 or seconds > 0:
                retstr += ", "
            count -= 1

        if days > 0:
            retstr += str(days)
            retstr += " days" if days > 1 else " day"
            if count == 2:
                retstr += " and "
            elif hours > 0 or minutes > 0 or seconds > 0:
                retstr += ", "
            count -= 1

        if hours > 0:
            retstr += str(hours)
            retstr += " hours" if hours > 1 else " hour"
            if count == 2:
                retstr += " and "
            elif minutes > 0 or seconds > 0:
                retstr += ", "
            count -= 1

        if minutes > 0:
            retstr += str(minutes)
            retstr += " minutes" if minutes > 1 else " minute"
            if seconds > 0:
                retstr += " and "

        if seconds > 0:
            retstr += str(seconds)
            retstr += " seconds" if seconds > 1 else " second"

        return retstr




def main():
    # "1 second"
    print(Solution().format_duration(1))

    # "1 minute and  2 minutes"
    print(Solution().format_duration(62))

    # "2 minutes"
    print(Solution().format_duration(120))

    # "1 hour"
    print(Solution().format_duration(3600))

    #  "1 hour, 1 minute and 2 seconds"
    print(Solution().format_duration(3662))

    # 4 years, 68 days, 3 hours and 4 minutes
    print(Solution().format_duration(132030240))

if __name__ == '__main__':
    main()