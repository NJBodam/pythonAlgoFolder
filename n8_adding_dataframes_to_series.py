import pandas as pd

# Change False to True for each block of code to see what it does

# Adding a Series to a square DataFrame
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s
    
    #Output:
    #     0    1    2    3
    # 0  10   50   90  130
    # 1  20   60  100  140
    # 2  30   70  110  150
    # 3  40   80  120  160
    #
    #     0   1   2   3
    # 0  11  52  93  134   (10 + 1, 50 + 2, 90 + 3, 130 + 4)
    # 1  21  62  103 144    (20 + 1, 60 + 2, 100 + 3, 140 + 4)
    # 2  31  72  113 154    (30 + 1, 70 + 2, 110 + 3, 150 + 4)
    # 3  41  82  123 164    (40 + 1, 80 + 2, 120 + 3, 160 + 4)


# Adding a Series to a one-row DataFrame 
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    print df
    print '' # Create a blank line between outputs
    print df + s

    #Output:
    #     0   1   2   3
    # 0  10  20  30  40
    #
    #     0   1   2   3
    # 0  11  22  33  44   (10 + 1, 20 + 2, 30 + 3, 40 + 4)


# Adding a Series to a one-column DataFrame
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
    print df
    print '' # Create a blank line between outputs
    print df + s

    #Output:

#     0
# 0  10
# 1  20
# 2  30
# 3  40

#     0   1   2   3
# 0  11 NaN NaN NaN
# 1  21 NaN NaN NaN
# 2  31 NaN NaN NaN
# 3  41 NaN NaN NaN

    
# Adding when DataFrame column names match Series index
if False:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s

    #Output:
    #     a    b    c    d
    # 0  10   50   90  130
    # 1  20   60  100  140
    # 2  30   70  110  150
    # 3  40   80  120  160
    #
    #     a   b   c   d
    # 0  11  52  93  134   (10 + 1, 50 + 2, 90 + 3, 130 + 4)
    # 1  21  62  103 144    (20 + 1, 60 + 2, 100 + 3, 140 + 4)
    # 2  31  72  113 154    (30 + 1, 70 + 2, 110 + 3, 150 + 4)
    # 3  41  82  123 164    (40 + 1, 80 + 2, 120 + 3, 160 + 4)


# Adding when DataFrame column names don't match Series index
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s

    #     a   b    c    d
    # 0  10  50   90  130
    # 1  20  60  100  140
    # 2  30  70  110  150
    # 3  40  80  120  160

    #     a   b   c   d   0   1   2   3
    # 0 NaN NaN NaN NaN NaN NaN NaN NaN
    # 1 NaN NaN NaN NaN NaN NaN NaN NaN
    # 2 NaN NaN NaN NaN NaN NaN NaN NaN
    # 3 NaN NaN NaN NaN NaN NaN NaN NaN
