import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
import tkinter

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    ])

sia = SentimentIntensityAnalyzer()



def tkinter():
    window = tk.Tk() 
    window.minsize(width="300",height="300")
    window.maxsize(width="500",height="500")

    def nltk_func():
        entryText = entryName.get() 
        labelName1.insert("")
        if entryText == " ":
            labelName1.insert('enter text')
        else:
            labelName1.insert("1.0",sia.polarity_scores(entryText))

    labelName = tk.Label(text = "  ")
    labelName.pack()

    entryName = tk.Entry()
    entryName.pack()

    buttonName = tk.Button(text="submit", command = nltk_func)
    buttonName.pack()


    labelName1 = tk.Label(text = "")
    labelName1.pack()


    window.mainloop() 
tkinter()
