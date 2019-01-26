#!/usr/bin/python
import sqlite3, bcrypt, argparse, json

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='GoPhish password updater and API key grabber.\nBuilt by @OneLogicalMyth')
parser.add_argument('--db', help='GoPhish database file path', default='gophish.db')
parser.add_argument('--newpass', help='New password to use for GoPhish', default='gophish')
args = parser.parse_args()

con = sqlite3.connect(args.db)
with con:
    cur = con.cursor()
    cur.execute("SELECT api_key,hash FROM users WHERE username == 'admin'")
    con.commit()
    row = cur.fetchone()
    api_key = row[0]
    old_hash = row[1]

b = bytearray()
new_hash = bcrypt.hashpw(bytes(args.newpass), bcrypt.gensalt(10,prefix=b'2a'))
con = sqlite3.connect(args.db)
with con:
    cur = con.cursor()
    cur.execute("UPDATE users SET hash=:hash WHERE username == 'admin'",{'hash':new_hash})
    con.commit()
    hash_updated = bool(cur.rowcount)

print json.dumps({'api_key':api_key,'old_hash':old_hash,'updated_hash':hash_updated},indent=4)
