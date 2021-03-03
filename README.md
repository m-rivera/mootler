# mootler
Your Moodle butler who gives usage reports from activity logs.

This is designed to work with UCL's Moodle implementation. It is not tested
anywhere else.

## Usage

Here is an example command:
```
moot activity.csv -u students.csv -s Potions -i -p
```

- `activity.csv` : Activity log for your module. It is recommended to filter for
    "participation" type activities.
- `-u students.csv`: (Optional) User list downloadable from Moodle. Only the
    users in the list will be considered, this way you can e.g. exclude tutor
    activity from your analysis.
- `-s Potions`: (Optional) Filter by "Event context". Just include a substring
    of what you care about, so if you want to see how many people have clicked
    on "File 2: Potions", you can just write `Potions` as long as no other
    activity contains the word.
- `-i`: (Optional) Save a list of inactive users as a csv file called
    `inactive.csv` by default.
- `-p` : (Optional) Plot the activity as a histogram by user.

