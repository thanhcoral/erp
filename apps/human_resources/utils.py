
def lv(group):
    group = group.strip()
    switcher={
        'Sys Admin': 0,
        'Sub Admin': 1,
        'HR': 2,
        'Inquiries': 10
    }
    return switcher.get(group,10)