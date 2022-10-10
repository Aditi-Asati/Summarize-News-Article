# for graphical user interface
import tkinter as tk

# following are three NLP(Natural Language Processing) libraries we are gonna use
import nltk
# used for sentiment analysis
from textblob import TextBlob
# python library used for web scraping articles
from newspaper import Article

nltk.download("punkt")


def summarize():
    """
    displays the title, author(s), publish date, summary, sentiment of the news article when the "Summarize" button is clicked on the GUI
    """
    #obtaining the url entered by the user on the GUI
    url = upt.get("1.0", "end").strip() # strip() is used to remove "\n" at the end of the url
    # creating an instance of the Article class
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # we cannot edit anything if the state is disabled, hence changing the state to normal
    title.config(state="normal")
    author.config(state="normal")
    publish.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    # inserting the title of the news article in the "title" text on GUI
    title.delete("1.0", "end")
    title.insert('1.0', article.title)

    # inserting the authors of the news article in the "author" text on GUI
    author.delete("1.0", "end")
    author.insert("1.0", article.authors)

    # inserting the publish date of the news article in the "publish" text on GUI
    publish.delete("1.0", "end")
    publish.insert("1.0", article.publish_date)

    # inserting the summary of the news article in the "summary" text on GUI
    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    # inserting the polarity and sentiment of the news article in the "sentiment" text on GUI
    sentiment.delete("1.0", "end")
    analysis = TextBlob(article.text)
    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state="disabled")
    author.config(state="disabled")
    publish.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

    # one can also perform the sentiment analysis on the summary of the news article

    # print(analysis.polarity)

    # print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"} ')

# coding the GUI (Graphical user Interface)
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1500x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state = "disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publish = tk.Text(root, height=1, width=140)
publish.config(state="disabled", bg="#dddddd")
publish.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

upt = tk.Text(root, height=1, width=140)
upt.pack()

button = tk.Button(root, text="Summarize", command=summarize)
button.pack()
root.mainloop()
print("Summarized successfully!")