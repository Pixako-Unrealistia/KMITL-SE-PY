

def time24hourTo12hour(time):
    time = [int(x) for x in time.split(":")]
    if time[0] == 0:
        return(f"12:{time[1]} AM")
    if time[0] > 12:
        time[0] - 12
        return(f"{time[0]}:{time[1]} PM")
    return(f"{time[0]}:{time[1]} AM")
print(time24hourTo12hour("00:12"))
