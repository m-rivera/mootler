"""
Class containing activity and users from Moodle output

"""
import pandas as pd

def users_to_fullnames(users_df):
    """Returns a list a full names from users DataFrame"""
    first_names = list(users_df["First name"])
    surnames = list(users_df["Surname"])

    full_names = [i + " " + j for i,j in zip(first_names, surnames)]
    return full_names

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

    def __repr__(self):
        n_activities = len(self.activity)
        n_users = len(self.users)
        out_str = "CourseData: {} activities, {} students".format(n_activities, n_users)
        return out_str

    def __str__(self):
        return self.__repr__()

    def filter_users(self):
        """Remove activities from users not from list"""
        names = users_to_fullnames(self.users)
        self.activity = self.activity[self.activity["User full name"].isin(names)]
        return






