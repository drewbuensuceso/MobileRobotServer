#this outputs the "data" in openCV system by matching the keyboard position with the normal keyboard(no changed positions)

#password = 'ah1296' sample password input
numkeyb_layout = '1 2 3\n4 5 6\n7 8 9\n0' #keyboard templates
letterKeyb_layout = 'q w e r t y u i o p \na s d f g h j k l \nz x c v b n m'
fullLetterKeyb_layout = '1 2 3 4 5 6 7 8 9 0 \nq w e r t y u i o p \na s d f g h j k l \nz x c v b n m'
#keyboard1 = '5 2 3\n9 8 1\n9 6 4\n7 1' #sample keyboard string
#keyboard2 = '1 8 2\n3 4 9\n6 5 0\n7 4' #sample keyboard string


def solve_numericalKeyb(keyboard,password):
    numkeyb = numkeyb_layout.split(sep=None)
    keyb_dict = dict(zip(keyboard,numkeyb))
    data = [keyb_dict.get(key) for key in password]
    return(data)

def solve_letterKeyb(keyboard, password):
    letterKeyb = letterKeyb_layout.split(sep=None)
    keyb_dict = dict(zip(keyboard,letterKeyb))
    data = [keyb_dict.get(key) for key in password]
    return(data)

def solve_fullLetterKeyb(keyboard, password):
    cpkeyb_values = fullLetterKeyb_layout.split(sep=None)
    cpkeyb_index = list(range(0,len(cpkeyb_values)))
    keyb_dict = dict(zip(cpkeyb_values,cpkeyb_index))
    data = [keyb_dict.get(key) for key in password]
    return(data)