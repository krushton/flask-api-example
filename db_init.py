import sqlite3
import sys
DATABASE = 'data.db' 


def db_init(table, column_string):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute('CREATE TABLE if not exists ' + table + '(' + column_string + ')')
    connection.commit()

if __name__ == '__main__':
    num_args = len(sys.argv)
    columns = []
    if num_args < 2:
        print 'Error: Incorrect arg format. Correct format is tablename column:type column:type ...'
        sys.exit()
    table = sys.argv[1].lower()
    for item in sys.argv[2:]:
        if ':' not in item:
            print 'Error: Must provide column name and data type separated by :'
            sys.exit()
        val_arr = [x.lower() for x in item.split(':')]
        columns.append(' '.join(val_arr))
    columns = ','.join(columns)
    db_init(table, columns)

