#!/usr/bin/python3

import requests

MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    result = requests.get(MYAPI).text.strip("\n")
    print(result.json())
    if result == "1":
        print("You won!")
    else:
        print("You lost!")

    return


if __name__ == "__main__":
    main()
