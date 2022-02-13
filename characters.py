import cv2 as cv
from cv2 import sumElems
import numpy as np

chars="# +-*=.ABCDEFGHIJKLMNOPQRSTUVWXYZ'0123456789?abcdefghijklmnopqrstuvwxyz|~"
chars="# +-*=.ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'|~"
sums_chars=[]

for char in chars:
    frame= np.zeros((50,50))
    frame= cv.putText(frame, char, (20, 30), cv.FONT_HERSHEY_PLAIN, 1, 255, 1)
    sum= np.sum(frame)
    #print(sum)
    sums_chars.append((char,int(sum)))
    #cv.imshow('char', frame)
    #if cv.waitKey(0) == ord('q'): break
cv.destroyAllWindows()
sums_chars= sorted(sums_chars, key= lambda sum_char: sum_char[1])
#print(sums_chars)
for sum_char in sums_chars: print(sum_char[0], end= '')




#