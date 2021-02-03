#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    date = "date=2020-01-01"
    ## Call the webservice with our key
    #apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)
    apodurlobj  = urllib.request.urlopen(NASAAPI + '&' + date  + "&"  + nasacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))


    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])
    #print(BirthdayURL)
#https://api.nasa.gov/neo/rest/v1/feed?start_date=2019-11-11&api_key=1KPXBQ9JCzlbsSwrFkFL9w2xiJD2ho3ChVZnLyb6
    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()

