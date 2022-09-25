import pyshorteners

url = input("Enter the URL here: ")

pysh = pyshorteners.Shortener()
shortened_url = pysh.tinyurl.short(url)

print("Shortened URL: ",shortened_url)