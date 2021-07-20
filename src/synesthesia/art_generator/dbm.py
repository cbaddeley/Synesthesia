import sqlite3 as sql
import numpy as np
import os
import io
import pickle


def retrieve(c, path, date, frq_selection, sr_selection):
    try:
        c.execute("""
            select notes, genre
            from samples 
            where path == ? and date == ? and frq_selection == ? and sr_selection == ?
            """, (path, date, frq_selection, sr_selection))
        return c.fetchall()
    except sql.OperationalError:
        return []


def insert(c, path, date, frq_selection, sr_selection, notes, genre):
    files = retrieve(c, path, date, frq_selection, sr_selection)
    if files == []:
        c.execute('insert into samples values(?,?,?,?,?)',
                  (path, date, frq_selection, sr_selection, pickle.dumps(notes), genre))



def get_samples(c):
    try:
        c.execute('select path, date from samples order by path asc')
        samples = c.fetchall()
        ret =[]
        # check if there are any file paths that are no longer valid, and purge them from the db
        for samp in samples:
            path, date = samp
            if not (os.path.exists(path) and str(os.path.getmtime(path)) == date):
                c.execute('delete from samples where path = ? and date = ?',
                        (path, date))
            else:
                if path not in ret:
                    ret.append(path)
        return ret
    except sql.OperationalError:
        return []

def get_specs(c, path):
    if path == '':
        return []
    c.execute('select frq_selection, sr_selection from samples where path = ?',(path,))
    return c.fetchall()
 
def db_driver(action, path='', frq_selection=0, sr_selection=0, notes='', genre=''):
    db_path = __file__[:-6] + 'audio_samples.db'
    ret = ''
    if not os.path.exists(db_path):
        conn = sql.connect(db_path)
        c = conn.cursor()
        c.execute("""
            create table samples (
                path text, 
                date text,
                frq_selection text,
                sr_selection text,
                notes blob,
                genre text
                )
            """)
        conn.commit()
        conn.close()
    conn = sql.connect(db_path)
    c = conn.cursor()
    if action.lower() == 'i':  # insert
        insert(c, path, str(os.path.getmtime(path)), str(frq_selection),
               str(sr_selection), notes, genre)
    elif action.lower() == 'r':  # retrieve all
        ret = retrieve(c, path, str(os.path.getmtime(path)),
                       str(frq_selection), str(sr_selection))
    elif action.lower() == 's':  # retrieve samples
        ret = get_samples(c)
    elif action.lower() == 'ss': # retrieve sample specs
        ret = get_specs(c, path)
    conn.commit()
    conn.close()
    return ret
