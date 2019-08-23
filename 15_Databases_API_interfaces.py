##### I skipped DATAbases chapter.

# pyhton database API

# db-api is a consolidated interface for a number of database systems. Every database engine has its own 
## interface, its own requirements, and really its own paradigm, so no single interface
# python ships with SQL lite. SQL lite is a fully functional, cross-platform DB system that's suitable for 
# many online and mobile application

import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('create')
    cur.execute()




















