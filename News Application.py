#This application uses News API and Tkinter

import requests 
import tkinter as tk

def getNews():
    api_key = "69098ca7575f42069325e5168a565e07"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news = requests.get(url).json()
    headings=news['articles']    #this has a list of dictioanary;each dictionary has 1 element which contains key ,value pairs
    #print(headings)
    articles = []
    news_articles = ""   #This to build up one text with all the news headings

    for i in headings:
        articles.append(i["title"])
    for i in range(len(headings)):
        news_articles = news_articles + str(i+1) + ". " + articles[i] + "\n"

    label.config(text = news_articles)#This widget implements a display box where you can place text or images.
 
root = tk.Tk()#Create the main window (container)
root.geometry("1000x800") #size of window
root.title("News Application")

button = tk.Button(root, font = 10, text = "Reload", command = getNews)
button.pack(pady = 50)#padding(space) around the button 

label = tk.Label(root, font = 12, justify = "center")
label.pack(pady = 20)

getNews()

root.mainloop()
