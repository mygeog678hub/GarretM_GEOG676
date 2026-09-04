# The try / except block handles an error if the file does not exist
try:
    file = open(r"H:\DevSource\GarretM_GEOG676\GISDev\topic\09\nfl.txt", "r")

    nfl_teams = file.readlines()
    for line in nfl_teams:
        print(line)
    file.close()
except IOError:
    print("An error has occurred")