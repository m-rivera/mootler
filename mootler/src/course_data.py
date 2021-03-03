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

    def filter_by_string(self, substring, col, incomplete = False):
        """
        Remove activities missing a string

        Parameters
        ----------
        substring : str
            The substring which indicates the activities to keep
        col : str
            Column name where the substring is searched. If `incomplete`, this can be a substring of the column name.
        incomplete : bool
            Only require a substring of the column name. (default: False)


        """
        # filtering by substring of column name
        if incomplete:
            columns = list(self.activity.columns)
            # use masking to filter column names containing substring
            mask = [col in i for i in columns]
            filtered_cols = [i for i,j in zip(columns,mask) if j]
            if len(filtered_cols) == 0:
                raise KeyError("Substring absent from any column names. Use a substring that identifies a column name.")
            elif len(filtered_cols) > 1:
                raise KeyError("Several (" + str(len(filtered)) +") column names contain substring. Use a substring that is only found once.")
            else:
                # filter
                self.activity = self.activity[self.activity[filtered_cols[0]].str.contains(substring)]
        # filtering with exact column name
        else:
            self.activity = self.activity[self.activity[col].str.contains(substring)]
        return

    def filter_by_context(self, substring):
        """
        Remove activities missing a string from Event Context

        Parameters
        ----------
        substring : str
            The substring which indicates the activities to keep

        """

        self.filter_by_string(substring, "Event context")
        return


