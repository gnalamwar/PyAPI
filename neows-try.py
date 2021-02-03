#!/usr/bin/python3
import requests
## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = 'api_key='+nasacreds.strip("\n")
    print(nasacreds)
    startdate = 'start_date=2020-05-16'
    print(startdate)
    neowrequest = requests.get(NEOURL + startdate + '&' + nasacreds)
    print(neowrequest)
    neodata = neowrequest.json()
    print(neodata)
    print(type(neodata))
    asteroid_sizes = {}
    asteroid_names = []
    danger_count=0
    print(f"Total Astroids in Range:", neodata["element_count"])
    for date in neodata["near_earth_objects"].keys():
        print(date)
        for aster in neodata["near_earth_objects"][date]:
            print(aster["name"])
            asteroid_sizes[aster["name"]] = aster["estimated_diameter"]["meters"]["estimated_diameter_max"]
            print(asteroid_sizes[aster["name"]])
            asteroid_names.append(aster["name"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1
    print(f"Largest Asteroid (meters): {max(asteroid_sizes)}") 
    print(f"Number of Potentiallu hazardous asteriods: {danger_count}")
    print(f"Asteroid Names : {asteroid_names}")
if __name__ == '__main__':
    main()

