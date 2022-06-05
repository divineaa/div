
#HOW TO DO CRUD

#SELECT QUERY
#SELECTS ONE PARTICULAR ITEM
author1 = Author.query.get(1) #CHANGE 1 TO ID

#SELECTS ALL RECORDS:
all_books = Book.query.all()

#SELECTS RELATED OBJECTS (CHECK REFERENTIAL INTEGRITIES)
#Suppose you want to fetch all the books of an author with id =2. This is one to many
author2 = Author.query.get(2)
author2_books = author2.books.all()# we use .all() since an author has many books
for i in author2_books:
    print(i.title)

#How about many to one
book2 = Book.query.get(2)
book2_author_id = book2.author_id
print(book2_author_id)

# FILTERING:
books_in_1594 = Book.query.filter(Book.year == 1594).all()

#ADVANCED FILTERING:
books_by_year = Book.query.order_by(Book.year).all()

#JOINS:
#joining 2 tables
results = db.session.query(tblname1, tblname2).join(tblname2).all() #tblname2 is the dependent tel

for tblname1, tblname2 in results:
	#access columns thru tlbname.colname

#joining 3 tables
results = db.session.query(tblname1, tblname2, tblname3). \
		select_from(tblname1).join(tblname2).join(tblname3).all() 

for tblname1, tblname2, tblname3 in results:
	#access columns thru tlbname.colname

#filters multiple columns
# Using filter() (and operator)
query = db.Session.query(User).filter(
    User.firstname.like(search_var1),
    User.lastname.like(search_var2)
    )

# Using filter_by() (and operator)
query = db.Session.query(User).filter_by(
    firstname.like(search_var1),
    lastname.like(search_var2)
    )

# Chaining filter() or filter_by() (and operator)
query = db.Session.query(User).\
    filter_by(firstname.like(search_var1)).\
    filter_by(lastname.like(search_var2))

# Using or_(), and_(), and not()
from sqlalchemy import and_, or_, not_

query = db.Session.query(User).filter(
    and_(
        User.firstname.like(search_var1),
        User.lastname.like(search_var2)
    )
)
#inserting entries:
a1 = Author(id = 1, first_name = "john" , last_name = "doe", email = "johndo@gmail.com")
db.session.add(a1)
db.commit()

# deleting entries/rows:
db.session.delete(Book.query.get(6))

#updating entries:
#first step is to get the id and assign the changes:
author_id1  = Author.query.get(1)
author_id1.email = "johndoe2022@gmailcom"
db.session.commit()