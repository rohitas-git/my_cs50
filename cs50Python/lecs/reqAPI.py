import requests # package that allows your program to behave as a web browser would.
import sys
import json # JSON library that can help us interpret the data received


entity = "song"
count = 10
artist = "Bruce Falconer"

def main():
    response = get_response()
    print_3(response)
    

def get_response():
    api_uri = f"https://itunes.apple.com/search?entity={entity}&limit={count}&term={artist}" 
    response = requests.get(api_uri)
    return response

def print_1(response):
    # The format in the downloaded text file is called JSON,
    print(response.json())
    
    
def print_2(response: requests.Response):
    print(json.dumps(response.json(), indent=2))
    
    
def print_3(response: requests.Response):
    t = response.json()
    for result in t["results"]:
        print(result["trackName"]) 
    
    
if __name__ == "__main__":
    main()
else:
    print(__name__) # equal to name of the file