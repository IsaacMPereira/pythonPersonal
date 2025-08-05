import webbrowser, sys, pyperclip

def main():
    if len(sys.argv) > 1:
        addres = ' '.join(sys.argv[1:])
    else:
        addres = pyperclip.paste()

    webbrowser.open(f'https://www.google.com/maps/search/{addres}')

if __name__ == '__main__':
    main()