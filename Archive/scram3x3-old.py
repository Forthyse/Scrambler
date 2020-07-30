from random import randint

# Standard scramble: 17-25
# Include double moves (Ex: R2, F2, etc.)
# Exclude double layer moves (Ex: r, u, etc.)
# Exclude rotational moves (x, y, z, etc.)
# Exclude slice moves (M, E, S, etc.)
# U(2)/U' = excl: U(2), U', D(2), D'
# D(2)/D' = excl: U(2), U', D(2), D'
# F(2)/F' = excl: F(2), F', B(2), B'
# B(2)/B' = excl: F(2), F', B(2), B'
# R(2)/R' = excl: R(2), R', L(2), L'
# L(2)/L' = excl: R(2), R', L(2), L'
# Moves: U, U', U2, D, D', D2, F, F', F2, B, B', B2, R, R', R2, L, L', L2
# Separate moves using spaces only
# Int length later by adding length parameter
# In the future maybe allow moves like: (L, R)
moves = ["U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2", "R", "R'", "R2", "L", "L'", "L2"]
# def scramble_3_length_set(slmin, slmax):
#     length = randint(slmin, slmax)
#     return length


# def scramble_3_integer():
#     value = randint(0, 17)
#     return value


# def scramble_3_assignment(integer):
#     if integer == 0:
#         character = 'U'
#         return character
#     elif integer == 1:
#         character = "U'"
#         return character
#     elif integer == 2:
#         character = 'U2'
#         return character
#     elif integer == 3:
#         character = 'D'
#         return character
#     elif integer == 4:
#         character = "D'"
#         return character
#     elif integer == 5:
#         character = 'D2'
#         return character
#     elif integer == 6:
#         character = 'F'
#         return character
#     elif integer == 7:
#         character = "F'"
#         return character
#     elif integer == 8:
#         character = 'F2'
#         return character
#     elif integer == 9:
#         character = 'B'
#         return character
#     elif integer == 10:
#         character = "B'"
#         return character
#     elif integer == 11:
#         character = 'B2'
#         return character
#     elif integer == 12:
#         character = 'R'
#         return character
#     elif integer == 13:
#         character = "R'"
#         return character
#     elif integer == 14:
#         character = 'R2'
#         return character
#     elif integer == 15:
#         character = 'L'
#         return character
#     elif integer == 16:
#         character = "L'"
#         return character
#     elif integer == 17:
#         character = 'L2'
#         return character


def check_for_dupes(s, sl, d1, d2, d3):
    """
    Checks to see if any "dupes" exist
    in the string according to the included tuples
    \n
    Arguments: \n
    s - Scramble list \n
    sl - Scramble length \n
    d1 through d3 - Dupe tuples \n
    """
    # Runs scramble_length time (shortens by 2 to ensure no calls to a non existent index are made)
    for x in range(0, sl - 1):
        # Checks if there is a dupe from the first tuple,
        # if so it replaces it and reruns to ensure it didn't create a new dupe)
        while (s[x] in d1) and (s[x + 1] in d1):
            s.insert(x + 1, moves[randint(0, 17)])
            s = check_for_dupes(s, sl, d1, d2, d3)
        # Second dupe check
        while (s[x] in d2) and (s[x + 1] in d2):
            s.insert(x + 1, moves[randint(0, 17)])
            s = check_for_dupes(s, sl, d1, d2, d3)
        # Third dupe check
        while (s[x] in d3) and (s[x + 1] in d3):
            s.insert(x + 1, moves[randint(0, 17)])
            s = check_for_dupes(s, sl, d1, d2, d3)
    # Returns the new, un-duplicated list
    return s



def dcheck(s, *args):
    if len(s) % 2 == 0:
        # Even length
        def deven(s, args):
            pre = s[0]
            nex = s[2]
            pas = True
            for x in s:
                if pas:
                    pass
                elif ((x in args[0]) or (x in args[1]) or (x in args[2])):
                    print('It was there')
    else:
        # Odd Length
        def dodd(s, args):
            pass

dcheck([1,2,3,4,5,6,7], (1,2,3), (True, False, True))
# ==============Main Function=================
# def scramble3x3(slmin, slmax):
#     """
#     Given a scramble length, will return a randomized list of scramble combos
#     """
#
#     dupe_1 = ('U', "U'", 'U2', 'D', "D'", 'D2')
#     dupe_2 = ('F', "F'", 'F2', 'B', "B'", 'B2')
#     dupe_3 = ('R', "R'", 'R2', 'L', "L'", 'L2')
#
#     scramble = []
#
#     # Sets the scramble_length
#     scramble_length = randint(slmin, slmax)
#     print(scramble_length)
#     # Assigns a character based on random integer input (Creates the scramble list)
#     for _ in range(0, scramble_length + 1):
#         scramble.append(moves[randint(0, 17)])
#     print(scramble)
#     # Checks for "dupes"
#     scramble = check_for_dupes(scramble, scramble_length, dupe_1, dupe_2, dupe_3)
#     scramble = ' '.join(scramble)
#     return scramble
#
#
# print(scramble3x3(17, 25))
# This is used for testing and will be removed later.