import pytest
import os


def test_database_directory():
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    assert os.path.exists(dbdir) is True


def test_database_file():
    root = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(root, '../database/db.sqlite')
    assert os.path.exists(database) is True
