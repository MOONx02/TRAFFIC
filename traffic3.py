import urllib.request, json

def get_traffic_time(origin, destination, api_key):
    # encode addresses for use in URL
    origin = urllib.parse.quote(origin)
    destination = urllib.parse.quote(destination)

    # create URL for API request
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=2801+kelvin+ave,+irvine,+ca,+92614&destination=15540+rockfield+blvd,+irvine,+ca&key=AIzaSyC5dwh8ERpsgT0GCgzV78yUm5Zf9OzYkME"

    # get API response and read it as JSON
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    # extract duration in traffic from response
    duration_in_traffic = data["routes"][0]["legs"][0]["duration_in_traffic"]["text"]

    # parse duration string to get minutes as integer
    duration_in_minutes = int(duration_in_traffic.split(" ")[0])

    return duration_in_minutes

# example usage
origin = "2801 Kelvin Ave, Irvine, CA 92614"
destination = "15540 Rockfield Blvd, Irvine, CA 92618"
api_key = "AIzaSyC5dwh8ERpsgT0GCgzV78yUm5Zf9OzYkME"

traffic_time = get_traffic_time(origin, destination, api_key)
print(f"The traffic time is {traffic_time} minutes.")
