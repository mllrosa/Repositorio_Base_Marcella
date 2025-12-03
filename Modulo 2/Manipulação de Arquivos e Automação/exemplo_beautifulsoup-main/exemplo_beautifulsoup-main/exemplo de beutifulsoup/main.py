import bs4

exampleFile = open('index3.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select('#author') #identificador author
sl = exampleSoup.select('.slogan') #classe slogan

print(elems[0]) #imprime o valor de id author
print(sl) #imprime o valor da classe slogan 