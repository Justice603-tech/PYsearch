# PYsearch
A python search engine
The python script sends an input to the user.
when the `user` types in the search query...the script opens up a url ex: `http://www.google.com/search?q=` following the input `variable`
and **BOOM!** search engine.
now i know that this is not a real search engine..but hey at least its cool.
source code here(you can also check the `PY` file):
```py
import webbrowser 
import time
print("Welcome to PYsearch. Please Enter a search query")
search = input(">>")
print(' Loading Search')
time.sleep(5)
webbrowser.open('http://www.google.com/search?q=' + search)



```
