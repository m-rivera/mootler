"""
Class containing activity and users from Moodle output

"""
import pandas as pd

def read_cd_csvs(acti_file, usr_file):
    """Read csv files to generate a CourseData object"""

    cdat = CourseData(pd.read_csv(acti_file),pd.read_csv(usr_file))
    return cdat

class CourseData(object):
    """
    Contains and processes data using an activity log and a user database

    Attributes
    ----------
    activity : DataFrame
        Log of activity on a Moodle course
    users : DataFrame
        Info on the users of interest (e.g. only students)

    """

    def __init__(self, activity, users):
        self.activity = activity
        self.users = users



