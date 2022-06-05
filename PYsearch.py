import webbrowser 
import time
print("Welcome to PYsearch. Please Enter a search query")
search = input(">>")
print(' Loading Search')
time.sleep(5)
webbrowser.open('http://www.google.com/search?q=' + search)


