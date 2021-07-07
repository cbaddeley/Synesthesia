import sqlite3 as sql
import numpy as np
import os
import io
import pickle


def retrieve(c, path, date, frq_selection, sr_selection):
    try:
        c.execute("""
            select frq, notes, genre
            from samples 
            where path == ? and date == ? and frq_selection == ? and sr_selection == ?
            """, (path, date, frq_selection, sr_selection))
        return c.fetchall()
    except sql.OperationalError:
        return ''

def insert(c, path, date, frq_selection, sr_selection, frq, notes, genre):
    files = retrieve(c, path, date, frq_selection, sr_selection)
    if files == []:
        print(type(frq))
        c.execute('insert into samples values(?,?,?,?,?,?,?)',
                  (path, date, frq_selection, sr_selection, pickle.dumps(frq), pickle.dumps(notes), genre))


def get_samples(c):
    try:
        c.execute('select path from samples order by path asc')
        return c.fetchall()
    except sql.OperationalError:
        return []


def db_driver(action, path, frq_selection, sr_selection, frq='', notes='', genre=''):
    db_path = __file__[:-6] + 'audio_samples.db'
    if not os.path.exists(db_path):
        conn = sql.connect(db_path)
        c = conn.cursor()
        c.execute("""
            create table samples (
                path text, 
                date text,
                frq_selection text,
                sr_selection text,
                frq blob, 
                notes blob,
                genre text
                )
            """)
        conn.commit()
    else:
        conn = sql.connect(db_path)
        c = conn.cursor()
        date = str(os.path.getmtime(path))
        frq_selection = str(frq_selection)
        sr_selection = str(sr_selection)
        if action.lower() == 'i':  # insert
            insert(c, path, date, frq_selection,
                   sr_selection, frq, notes, genre)
        elif action.lower() == 'r':  # retrieve
            return retrieve(c, path, date, frq_selection, sr_selection)
        elif action.lower() == 'l':  # list
            return get_samples(c)
        conn.commit()
    conn.close()
