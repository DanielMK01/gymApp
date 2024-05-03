import sqlite3
import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

import db

def test_create_db():
    try:
        db.create_db_table()
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        cur.execute("SELECT name from sqlite_master WHERE type='table' AND name='gymdays'")
        first = cur.rowcount()
        cur.execute("SELECT name from sqlite_master WHERE type='table' AND name='exercisedmuscle'")
        second = cur.rowcount()
        con.close()
        assert(first == 1)
        assert(second == 1)
    except:
        print("DB creation failed")

def test_add_em1():
    try:
        ename = "Push-ups"
        mname = "Compound-upper"
        db.add_em(ename, mname)
        con = sqlite3.connect("gymcache.db")
        cur = con.cursor()
        res = cur.execute("SELECT FROM exercisedmuscle WHERE ename = ? AND mname = ?", {ename, mname})
        comp = res.fetchone()
        con.close()
        db.delete_em(ename, mname)
        assert(comp[0] == ename and comp[1] == mname)
    except sqlite3.OperationalError:
        print("database has not yet been created")

# def test_add_exercise1():
#     try:
