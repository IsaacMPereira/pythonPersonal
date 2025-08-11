import sys
import webbrowser
import requests
import bs4

def main():
    z = len(sys.argv)
    if z <= 1:
        print("Error. Too few arguments")
        exit()

    print("Googling...")
    input = ' '.join(sys.argv)[1:]
    
    res = requests.get(f"https://www.google.com/search?q={input}")

    res.raise_for_status()

    output = open("output.html", "wb")
    for chunk in res.iter_content(1000000):
        output.write(chunk)
    
    output.close()

    exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = exampleSoup.select('.zReHs href')

    print(len(elems))

if __name__ == '__main__':
    main()