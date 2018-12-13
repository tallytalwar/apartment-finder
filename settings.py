import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2300

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'toronto'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["yrk", "tor"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "north york": [
        [43.773799, -79.443040],
        [43.647764, -79.354656],
    ],
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["north york", "york", "toronto"]

MIN_BED = 2
MIN_BATH = 1

MIN_FT2 = 800

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "Finch": [43.780983, -79.415170],
    "North York Centre": [43.768656, -79.412535],
    "Sheppard - Yonge": [43.761740, -79.411971],
    "York Mills": [43.744672, -79.407043],
    "Lawrence": [43.725367, -79.402479],
    "Eglinton": [43.705293, -79.398968],
    "Davisville": [43.697973, -79.397276],
    "St-Clair": [43.687483, -79.393086],
    "Summerhill": [43.682289, -79.390816],
    "Rosedale": [43.677174, -79.388585],
    "Bloor": [43.670784, -79.386963],
    "Wellesley": [43.665644, -79.383866],
    "College": [43.661345, -79.383107],
    "Dundas": [43.656290, -79.380506],
    "Queen": [43.652408, -79.379248],
    "King": [43.649182, -79.377902],
    "Union": [43.645463, -79.380588],
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housingtoronto"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
