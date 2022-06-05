from app import db
from app import User, Article, Comment
from textblob import TextBlob
import random
n = random.randint(0,1000)



#insert records into User
u1 = User(username = 'sam'+str(n) , email='sam'+str(n)+'@gmail.com', password_hash='password', firstname='sam', lastname='gregory', middlename='castillo')

db.session.add(u1)
db.session.commit()


#print the records of User Model
all_users = User.query.all()
for u in all_users:
    print("ID: " + str(u.id) + "| Username: " + u.username + "|Password " + u.password_hash)

#convert to string if int ex. str(intcolumn)

#insert records into Article
a1 = Article(title='sample', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum volutpat turpis sem, ut rhoncus magna euismod quis. Aenean mattis sem in dui venenatis, nec euismod nisl ornare. In ut eleifend justo. Mauris faucibus ipsum vitae urna gravida bibendum. Maecenas aliquam eros sit amet malesuada elementum. Cras condimentum, augue et auctor vestibulum, leo quam consequat nibh, sed posuere purus lacus in erat. Nulla id lacus fringilla nibh blandit vestibulum. Aliquam semper pellentesque justo ut efficitur. Donec porttitor auctor lacus. Nunc cursus dolor accumsan, pharetra ante id, interdum dui. Cras nisl nulla, egestas vel turpis et, pulvinar fermentum sem. Nam iaculis elementum mollis. Nullam placerat, libero ut tristique eleifend, sem mauris consectetur purus, id fringilla enim erat at nibh. </br> Vestibulum auctor augue eu tristique congue. Nullam iaculis feugiat lobortis. Morbi convallis magna sed sem rutrum, ac ultricies lectus dapibus. Donec molestie augue sit amet orci venenatis viverra. Aenean quis semper nisl, ut pharetra lacus. Maecenas cursus rhoncus est quis viverra. Praesent mollis consequat nisi aliquet lobortis. Aenean pellentesque faucibus dui, ac laoreet elit pharetra nec. In feugiat maximus erat sed pellentesque. Ut fermentum libero quis dui sodales condimentum. Vestibulum sed tellus porttitor, accumsan lectus eu, fermentum enim. Sed sagittis turpis quis leo gravida mattis. Suspendisse ac ex vel eros tincidunt euismod. Aliquam vehicula tempor est, pharetra convallis erat condimentum ac.', location = 'Baguio City', user_id=1)
db.session.add(a1)
db.session.commit()
#print records of Article Model
all_articles = Article.query.all()
for a in all_articles:
    print("ID: " + str(a.id) + "| Title: " + a.title + "location: " + a.location + " Author: " + str(a.user_id))

#insert records into Comment
def getPolarity(text):
    text=str(text)
    return TextBlob(text).sentiment.polarity

sentimento = 'The worst place ever'
score = getPolarity(sentimento)
sent_ana = 0
if score>=0:
    sent_ana = 1
else:
    sent_ana = 0

c1 = Comment(description = sentimento, location = 'Baguio City', sentiment_analysis = sent_ana, user_id = 1, article_id = 1)

db.session.add(c1)
db.session.commit()


#print the records of Comment Model
all_comments = Comment.query.all()
for c in all_comments:
    print("ID: " + str(c.id) + "| Username: " + str(c.user_id) + "|Comment " + c.description + " Analysis: " + str(c.sentiment_analysis))
