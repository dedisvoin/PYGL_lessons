from pygl_nf import GL # importing

win = GL.Display_init_() # creating a window instance

mouse = GL.Sub_events_.Mouse_init() # this is where the mouse initialization takes place
                                    # next, all actions will occur with this instance of the class

while win.CEU(): # rendering cycle
    pass