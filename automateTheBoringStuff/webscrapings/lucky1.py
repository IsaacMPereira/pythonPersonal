import sys, webbrowser

def main():
    z = len(sys.argv)
    if z <= 1:
        print("Error. Too few arguments")
        exit()

    s = ' '.join(sys.argv[1:])

    web = f'https://www.google.com/search?q={s}'

    webbrowser.open(web)

if __name__ == '__main__':
    main()