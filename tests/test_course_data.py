import mootler.src.course_data as cd

def test_read_cd_csvs():
    """Read actions and user list"""
    cdat = cd.read_cd_csvs("data/activity.csv","data/students.csv")
    assert cdat.users["First name"][0] == "Draco"

