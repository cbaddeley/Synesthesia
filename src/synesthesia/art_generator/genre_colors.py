from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

def getColors(genre):

    all_colors = [ 
    Qt.white,
    Qt.black,
    Qt.cyan,
    Qt.darkCyan,
    Qt.red,
    Qt.darkRed,
    Qt.magenta,
    Qt.darkMagenta,
    Qt.green,
    Qt.darkGreen,
    Qt.yellow,
    Qt.darkYellow,
    Qt.blue,
    Qt.darkBlue,
    Qt.gray,
    Qt.darkGray,
    Qt.lightGray ]

    genre_colors = {
        'rock'              : [], 
        'pop'               : [], 
        'alternative'       : [], 
        'indie'             : [QColor(244, 125, 74), QColor(225,45,90), QColor(255,236,92), QColor(0,141,203)],
        'electronic'        : [], 
        'female vocalists'  : [],
        'dance'             : [], 
        '00s'               : [], 
        'alternative rock'  : [], 
        'jazz'              : [], 
        'beautiful'         : [],
        'metal'             : [],
        'chillout'          : [], 
        'male vocalists'    : [],
        'classic rock'      : [],
        'soul'              : [],
        'indie rock'        : [], 
        'Mellow'            : [],
        'electronica'       : [],
        '80s'               : [], 
        'folk'              : [], 
        '90s'               : [],
        'chill'             : [],
        'instrumental'      : [], 
        'punk'              : [], 
        'oldies'            : [],
        'blues'             : [], 
        'hard rock'         : [], 
        'ambient'           : [],
        'acoustic'          : [], 
        'experimental'      : [],
        'female vocalist'   : [],
        'guitar'            : [], 
        'Hip-Hop'           : [],
        '70s'               : [], 
        'party'             : [], 
        'country'           : [],
        'easy listening'    : [], 
        'sexy'              : [], 
        'catchy'            : [],
        'funk'              : [], 
        'electro'           : [], 
        'heavy metal'       : [],
        'Progressive rock'  : [], 
        '60s'               : [],
        'rnb'               : [], 
        'indie pop'         : [], 
        'sad'               : [], 
        'House'             : [], 
        'happy'             : []
        }

    colors = genre_colors.get(genre)
    if colors is None or colors == []:
        colors = all_colors
    return colors