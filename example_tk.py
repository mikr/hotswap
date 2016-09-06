"""
To enable hotswapping for this example call:
    python hotswap.py example_tk.py
"""

from Tkinter import *

# This program shows how to use the "after" function to make animation.

class Test(Frame):
    def printit(self):
        print "hi"

    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT', foreground='red', 
                           command=self.quit)
        self.QUIT.pack(side=LEFT, fill=BOTH)

        self.draw = Canvas(self, width="5i", height="5i")

        # all of these work..
        self.draw.create_rectangle(0, 0, 10, 10, tags="thing", fill="blue")
        self.draw.pack(side=LEFT)

    def moveThing(self, *args):
        # move 1/10 of an inch every 1/10 sec (1" per second, smoothly)
        self.draw.move("thing", "0.01i", "0.01i")

        # change 100 to 500 while this example is running with hotswapping
        # enabled to see it moving slower with restart the program.
        self.after(100, self.moveThing)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.moveThing)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    # Command line arguments of the script to be run are preserved by the
    # hotswap.py wrapper but hotswap.py and its options are removed that
    # sys.argv looks as if no wrapper was present.
    print "argv:", `argv`
    test = Test()
    test.mainloop()

if __name__ == '__main__':
    main()
