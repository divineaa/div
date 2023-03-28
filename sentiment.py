from textblob import TextBlob
#insert records into Comment
def getSentimentScore(text):
    text=str(text)
    score = TextBlob(text).sentiment.polarity
    sent_ana = 0
    if score>=0.5:
        sent_ana = 1
    else:
        sent_ana = 0
    return sent_ana

