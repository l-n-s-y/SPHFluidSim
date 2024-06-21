"""
Contribution log colour map:
0  = blank   = ' ' 
1  = lightest= '-'
2  = light   = '*'
3  = dark    = '%'
4> = darkest = '#'

"""

import datetime
from debug_renderer import render,debug_render_image


char_to_pushcount_table = {
        " ": 0,
        "-": 1,
        "*": 2,
        "%": 3,
        "#": 4
}

"""
Generate an array of (datetime,push_count) tuples to describe
the provided ASCII img
"""
def generate_schedule(img,start_date=None):
    schedule = []

    start_offset = 0
    current_date = datetime.date.today()
    if start_date: # TODO: must be equal to current date or later
        start_date = start_date.date() # truncate to year-month-day
        start_offset = start_date - current_date
        current_date = start_date

    #for line in img.split('\n'):
    for line in img:
    #    for c in line:
        for c in line:
            #if c not in char_to_pushcount_table:
            #    print(f"{c} is not a valid char. you can only use {[char_to_pushcount_table[key] for key in char_to_pushcount_table]}")
            #    return None

            #current_char_push_timeslot = (current_date.isoformat(),char_to_pushcount_table[c])
            current_char_push_timeslot = (current_date.isoformat(),c)
            schedule.append(current_char_push_timeslot)

    return schedule

if __name__ == "__main__":
    
    image_to_render = debug_render_image

    contribution_schedule = generate_schedule(image_to_render)
    if not contribution_schedule: # I'm too lazy to make an exception for this
        print("failed to generate schedule")
        exit()

    print(contribution_schedule)

    render(image_to_render)
