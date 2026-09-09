def findPlatform(Arrival, Departure):
    n = len(Arrival)
    maxCount = 0

    for i in range(n):
        count = 0
        # Check how many trains are at the station when train 'i' arrives
        for j in range(n):
            # A train is at the station if its arrival is before or equal to train i's arrival,
            # and its departure is after or equal to train i's arrival.
            if Arrival[j] <= Arrival[i] <= Departure[j]:
                count += 1
        
        maxCount = max(maxCount, count)
        
    return maxCount
  
Arrival = [900, 940, 950, 1100, 1500, 1800]
Departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum platforms needed:", findPlatform(Arrival, Departure))