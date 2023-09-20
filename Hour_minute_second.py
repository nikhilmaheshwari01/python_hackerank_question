# Prompt the user to enter the number of seconds
seconds = int(input(""))

# Calculate the hours, minutes, and remaining seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60


print(seconds,"seconds is equivalent to",hours,"hours,",minutes,"minutes, and",remaining_seconds,"seconds.")