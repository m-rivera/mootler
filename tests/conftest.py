import os
import pytest
import mootler.src.course_data as cd

test_dir = os.path.dirname(os.path.abspath(__file__))
test_data_dir = os.path.join(test_dir, "data")

def _in_data(file_name):
    """Return absolute name of file in data/ dir"""
    return os.path.join(test_data_dir, file_name)


@pytest.fixture
def hogwarts_cd():
    """CourseData test set"""
    cdat = cd.read_cd_csvs(_in_data("activity.csv"),_in_data("students.csv"))
    return cdat

