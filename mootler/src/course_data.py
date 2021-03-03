"""
Class containing activity and users from Moodle output

"""
import pandas as pd
import plotly.express as px
from operator import itemgetter

def users_to_fullnames(users_df):
    """Returns a list a full names from users DataFrame"""
    first_names = list(users_df["First name"])
    surnames = list(users_df["Surname"])

    full_names = [i + " " + j for i,j in zip(first_names, surnames)]
    return full_names

def read_cd_csvs(acti_file, usr_file=None):
    """
    Read csv files to generate a CourseData object

    Parameters
    ----------
    acti_file : str
        Name of csv file containing the activities.
    usr_file : str
        Name of csv file containing users. Optional: if it's not included, cdat.users = None

    """
    if usr_file:
        cdat = CourseData(pd.read_csv(acti_file),pd.read_csv(usr_file))
    else:
        cdat = CourseData(pd.read_csv(acti_file), None)
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

    def active_users(self):
        """Return a list of users having done an activity"""
        ac_users = self.activity["User full name"].unique()
        return ac_users

    def count_unique_active_users(self):
        """Return number of unique active users"""
        n_ac_users = len(self.active_users())
        return n_ac_users

    def inactive_users(self):
        """Return a DataFrame of inactive users"""
        full_names = users_to_fullnames(self.users)
        active_names = self.active_users()
        # mask for inactivity
        mask = [i not in active_names for i in full_names]

        return self.users[mask]

    def plot_by_activity(self):
        """Show html bar plot of user activity"""
        user_names = self.active_users()
        activity_counts = [len(self.activity[self.activity["User full name"] == name]) for name in user_names]
        names_counts = zip(user_names,activity_counts)
        # sort
        sorted_names = [i[0] for i in sorted(names_counts,key=itemgetter(1),reverse=True)]
        # plot
        fig = px.histogram(self.activity, x="User full name")
        # reorder
        fig.update_xaxes(categoryorder = "array", categoryarray = sorted_names)
        fig.show()

        return


