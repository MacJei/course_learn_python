def get_sum(one, two, delimiter='&'):
    o = str(one)
    t = str(two)
    dm = f"{o}{delimiter}{t}"
    print(dm.upper())


get_sum('Learn', 'Python')