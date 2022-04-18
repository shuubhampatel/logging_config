"""This makes the test for log_test"""
import os

from click.testing import CliRunner

from app import create_log_folder, create_database

runner = CliRunner()


def log_folder_test():
    """This test for log folder existence check"""
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) is True


def database_check():
    """This test for database existence check"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
