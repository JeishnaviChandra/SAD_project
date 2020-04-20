from models import *
from create import app, db
import csv

def main() :
    data = open("books.csv") 
    read = csv.reader(data)
    c = 1
    for row in read :
        if c == 1:
            c=0
            continue
        b = Book(isbn=row[0], title=row[1], author=row[2], year=row[3])
        db.session.add(b)
    db.session.commit()

if __name__ == "__main__" :
    with app.app_context():
        main()