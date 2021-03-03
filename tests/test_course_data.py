import mootler.src.course_data as cd

def test_read_cd_csvs():
    """Read actions and user list"""
    cdat = cd.read_cd_csvs("data/activity.csv","data/students.csv")
    assert cdat.users["First name"][0] == "Draco"

def test_read_cd_csv_no_users():
    """Read actions but no users"""
    cdat = cd.read_cd_csvs("data/activity.csv")
    assert cdat.activity["User full name"][0] == "Harry Potter"

def test_tostring(hogwarts_cd):
    """Test CourseData tostring method"""
    assert hogwarts_cd.__str__() == "CourseData: 6 activities, 6 students"

def test_filter_users(hogwarts_cd):
    """Test filtering activity by user list"""
    hogwarts_cd.filter_users()
    assert len(hogwarts_cd.activity) == 5

def test_filter_by_string(hogwarts_cd):
    """Test filtering by string"""
    hogwarts_cd.filter_by_string("Potions", "Event context")
    assert len(hogwarts_cd.activity) == 3

def test_filter_by_string(hogwarts_cd):
    """Test filtering by incomplete column string"""
    hogwarts_cd.filter_by_string("Potions", "context", incomplete=True)
    assert len(hogwarts_cd.activity) == 3

def test_filter_by_context(hogwarts_cd):
    hogwarts_cd.filter_by_context("Potions")
    assert len(hogwarts_cd.activity) == 3

def test_count_unique_active_users(hogwarts_cd):
    assert hogwarts_cd.count_unique_active_users() == 5

def test_inactive_users(hogwarts_cd):
    inactive_users = hogwarts_cd.inactive_users()
    assert len(inactive_users) == 2
