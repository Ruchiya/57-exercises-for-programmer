import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

exist = "SELECT name FROM sqlite_master WHERE type='table' AND name='record'"
if not c.execute(exist).fetchone():
    c.execute('''
CREATE TABLE record
(first,
last,
position,
seperation_date)
''')

record = []

while True:
    field = input('Enter employee detail > ')
    if field == '':
        break
    else:
        new = field.split()
        if len(new) == 5:
            new[2] = new[2]+' '+new[3]
            new[3]= new[4]
            record.append(new[:4])
        elif len(new) == 3:
            new.append(' ')
            record.append(new)
        else:
            record.append(new)
        continue


c.executemany('INSERT INTO record VALUES(?,?,?,?)',record)

print('Name', ' '*17,'|', 'Position', ' '*12,'|','Seperation Date')
print('-'*65)
for row in c.execute('SELECT * FROM record ORDER BY last'):
    space = 20-len(row[0]+row[1])
    space1 = 20-len(row[2])
    print(row[0]+' '+row[1],space*' ','|',row[2],space1*' ','|',row[3])

c.close()
