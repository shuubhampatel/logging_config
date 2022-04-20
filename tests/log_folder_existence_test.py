"""This makes the test for log_test"""
import os

from click.testing import CliRunner

from app import create_log_folder, create_database

runner = CliRunner()


def test_log_folder():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs')
    assert os.path.exists(logdir) is True
