import librosa
import turtle
import numpy as np
from synesthesia.wsl import *
set_display_to_host()

# y, sr = librosa.load('../mp3/around_the_sun.mp3', sr=22050)
# C = librosa.cqt(y, sr)
# chroma = librosa.feature.chroma_cqt(C=C, sr=sr)
#
#
# turtle.screensize(canvwidth=400, canvheight=400)
# t = turtle.Turtle()
#
# no_img_chroma = []
# for i in chroma:
#     for j in i:
#         no_img_chroma.append([np.real(j), np.imag(j)])
#
# track = 0
# for x in no_img_chroma:
#     if x[0] != 0:
#         if track == 0:
#             t.rt(x[0]*50)
#             track += 1
#         elif track == 1:
#             t.fd(x[0]*50)
#             track += 1
#         elif track == 2:
#             t.lt(x[0]*50)
#             track += 1
#         elif track == 3:
#             t.bk(x[0]*50)
#             track = 0
