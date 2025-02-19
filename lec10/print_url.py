import sys
import urllib.request

URL = "http://info.cern.ch/hypertext/WWW/TheProject.html"

def print_data_url(url_name: str) -> None:
    response = urllib.request.urlopen(url_name)
    response_data = response.read()
    response.close()
    print(response_data)

if __name__ == "__main__":
    # print_data_url(sys.argv[1])
    user_url = input("Enter an URL: ")
    if not user_url:
        user_url = URL
    print_data_url(user_url)