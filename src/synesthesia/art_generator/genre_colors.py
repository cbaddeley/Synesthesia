from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

def hex_to_colors(hex_vals): # takes a list of hex vals and returns a list of QColor objects
    QColors = []
    for hex_val in hex_vals:
        rgb = tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))
        QColors.append(QColor(*rgb))
    return QColors

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
        'indie'             : ['F47D4A', 'E1315B', 'FFEC5C', '008DCB'],
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
    else:
        colors = hex_to_colors(colors)
    return colors