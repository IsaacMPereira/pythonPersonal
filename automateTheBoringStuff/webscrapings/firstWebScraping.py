import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('p')

print(type(elems))

print(len(elems))

print(type(elems[0]))

print(elems[0].getText())

print(str(elems[0]))

print(elems[0].attrs)