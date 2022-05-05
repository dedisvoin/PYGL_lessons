from pygl_nf import GL # importing

win = GL.Display_init_(flags=GL.D_Full) # creating a window instance

while win.CEU(): # rendering cycle

    win.GL.Rect('red',[100,100],[200,320],0,'s','D') # drawing a rectangle
#                 |       |         |        |    \
#              color  position    size     surf   drawing_function


    win.GL.Circle('green',[400,400],120,0,'s','D') # drawing a circle

    win.GL.Ellips(GL.Color_._rgb(100,220,180,0).COLOR,[600,600],[200,120],0,'s','D') # drawing a ellips

    win.GL.Line('brown',[100,500],[500,200],20,'s','R','D') # drawing line
    
