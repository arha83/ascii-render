import curses
from curses import wrapper
import time
import cv2 as cv


chars= " .'-I1~YJ|L7+=TVX*CFKSUZ023A45OP9H6DEGNQR8WBM#"

def scr(stdscr : curses.window):
    capture= cv.VideoCapture(1)
    #frame= cv.imread('./test.png')
    stdscr.nodelay(True)
    while True:
        ret, frame= capture.read()
        frame= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame= cv.resize(frame, (40,30))
        for i in range(40):
            for j in range(30):
                index= int(((len(chars)-1)*frame[j,i])/255.0)
                stdscr.addstr(j,i, chars[index])
        try:
            stdscr.getkey()
            break
        except: pass
        stdscr.refresh()
        time.sleep(1/30)
    capture.release()
    

wrapper(scr)

