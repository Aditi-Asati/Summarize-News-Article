# News Summarizer
- The program ```main.py``` in ```Summarize_News_Article ``` repo uses NLP libraries to convey the title, authors(s), publish date, summary, Polarity and sentiment of the news article as to whether is it written in a positive, negative or neutral note just by requiring the url of the news article.
- It is interactive in the sense that it uses a Graphical User Interface to communicate with the user.
- one needs to provide a url of a news article to the url text block on the GUI and then press the ```Summarize``` button to find out the details of the news article such as the title, summary, authors, publish_date, polarity etc.

- The program is great for incuisitive minds who don't have time to go through the entire news article.
- It saves the time of the readers! :)
# Installation
## Using Git
Type the following command in your Git Bash:

- For SSH:
```git clone git@github.com:Aditi-Asati/Summarize-News-Article.git```
- For HTTPS: ```git clone https://github.com/Aditi-Asati/Summarize-News-Article.git```

The whole repository would be cloned in the directory you opened the Git Bash in.

## Using GitHub ZIP download
You can alternatively download the repository as a zip file using the GitHub **Download ZIP** feature. 

*External modules used-*
- newspaper3k
- nltk 
- textblob

Run the command ```pip install -r requirements.txt``` to install all these dependencies at once.

You are good to go!