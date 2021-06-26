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
        'rock'              : ['00293C', '1E656D', 'F1F3CE', 'F62A00'],
        'pop'               : ['F98866', 'FF420E', '80BD9E', '89DA59'], 
        'alternative'       : ['00293C', '1E656D', 'F1F3CE', 'F62A00'],
        'indie'             : ['F47D4A', 'E1315B', 'FFEC5C', '008DCB'],
        'electronic'        : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'], 
        'female vocalists'  : ['F52549', 'FA6775', 'FFD64D', '9BC01C'],
        'dance'             : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'],
        '00s'               : ['F98866', 'FF420E', '80BD9E', '89DA59'], 
        'alternative rock'  : ['00293C', '1E656D', 'F1F3CE', 'F62A00'],
        'jazz'              : ['003B46', '07575B', '66A5AD', 'C4DFE6'], 
        'beautiful'         : ['F98866', 'FF420E', '80BD9E', '89DA59'], 
        'metal'             : ['626D71', 'CDCDC0', 'DDBC95', 'B38867'], 
        'chillout'          : ['F4CC70', 'DE7A22', '20948B', '6AB187'], 
        'male vocalists'    : ['363237', '2D4262', '73605B', 'D09683'],
        'classic rock'      : ['00293C', '1E656D', 'F1F3CE', 'F62A00'],
        'soul'              : ['2988BC', '2F496E', 'F9BA32', 'ED8C72'],
        'indie rock'        : ['F47D4A', 'E1315B', 'FFEC5C', '008DCB'],
        'Mellow'            : ['F4CC70', 'DE7A22', '20948B', '6AB187'],
        'electronica'       : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'],
        '80s'               : ['F77604', 'B8D20B', 'F56C57', '231B12'], 
        'folk'              : ['AF4425', '662E1C', 'EBDCB2', 'C9A66B'],
        '90s'               : ['C7DB00', '7AA802', 'F78B2D', 'E4B600'], 
        'chill'             : ['F4CC70', 'DE7A22', '20948B', '6AB187'],
        'instrumental'      : ['C7DB00', '7AA802', 'F78B2D', 'E4B600'], 
        'punk'              : ['F70025', 'F25C00', 'F9A603', 'FF4040'], 
        'oldies'            : ['2988BC', '2F496E', 'F9BA32', 'ED8C72'],
        'blues'             : ['003B46', '07575B', '66A5AD', 'C4DFE6'], 
        'hard rock'         : ['626D71', 'CDCDC0', 'DDBC95', 'B38867'], 
        'ambient'           : ['A1BE95', 'E2DFA2', '92AAC7', 'ED5752'],
        'acoustic'          : ['A1BE95', 'E2DFA2', '92AAC7', 'ED5752'], 
        'experimental'      : ['FFCE30', 'E83845', 'E389B9', '288BA8'],
        'female vocalist'   : ['F52549', 'FA6775', 'FFD64D', '9BC01C'],
        'guitar'            : ['AF4425', '662E1C', 'EBDCB2', 'C9A66B'],
        'Hip-Hop'           : ['004D47', '128277', '52958B', 'B026FF'],
        '70s'               : ['00293C', '1E656D', 'F1F3CE', 'B026FF'],
        'party'             : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'],
        'country'           : ['AF4425', '662E1C', 'EBDCB2', 'C9A66B'],
        'easy listening'    : ['F4CC70', 'DE7A22', '20948B', '6AB187'],
        'sexy'              : ['004D47', '128277', '52958B', 'B026FF'],
        'catchy'            : ['F98866', 'FF420E', '80BD9E', '89DA59'], 
        'funk'              : ['004D47', '128277', '52958B', 'B026FF'],
        'electro'           : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'],
        'heavy metal'       : ['626D71', 'CDCDC0', 'DDBC95', 'B38867'], 
        'Progressive rock'  : ['00293C', '1E656D', 'F1F3CE', 'F62A00'],
        '60s'               : ['003B46', '07575B', '66A5AD', 'C4DFE6'], 
        'rnb'               : ['003B46', '07575B', '66A5AD', 'C4DFE6'], 
        'indie pop'         : ['F98866', 'FF420E', '80BD9E', '89DA59'], 
        'sad'               : ['003B46', '07575B', '66A5AD', 'C4DFE6'], 
        'House'             : ['4CB5F5', 'E6D72A', 'F18D9E', 'B3C100'],
        'happy'             : ['F52549', 'FA6775', 'FFD64D', '9BC01C']
        }

    colors = genre_colors.get(genre)
    if colors is None or colors == []: # if genre not found, assigns list of 20 random git colors
        colors = all_colors
    else:
        colors = hex_to_colors(colors)
    return colors