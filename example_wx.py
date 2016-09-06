"""
This example describes features and gotchas in using the
hotswap module to speed up development.

To enable hotswapping for this example call:
    python hotswap.py example_wx.py
"""

import sys
import wx

def onHotswap():
    """Called when the source of this module has changed.

    When a function named 'onHotswap' is present in a module,
    this function is called after the module is reloaded.
    This should be used to trigger a redisplay of the screen or
    in general to discard cached results that are to be calculated
    again using the new method definitions.

    If onHotswap is not defined the module is reloaded anyway, but afterwards
    no further actions are performed. In this case the changed code has to be
    activated some other way like minimizing and restoring the window to be
    repainted.
    """
    # Trigger a repaint of the main window that the updated paint method
    # is immediately called after saving the changed source file.
    wx.GetApp().GetTopWindow().Refresh()

class TestFrame(wx.Frame):
    def __init__(self, parent, id=-1):
        wx.Frame.__init__(self, None, id, title="Hotswap wxPython Test",
                 pos = (1605, 5),
                 size=(300, 300))

        # The method OnPaint is registered inside wxPython and
        # therefore not replaced automatically.
        wx.EVT_PAINT(self, self.OnPaint)
        wx.EVT_CHAR(self, self._OnChar)

        # Code inside a constructor is changed by a reload, but as you know
        # the constructor of an object is called only once during creation.
        # So if you change the value of circle_x, the new value is only used
        # after a program restart.
        self.circle_x = 150

    def init(self):
        """On demand constructor.

        This constructor is called for every repaint. Therefore in general the
        existence of an object attribute has to be checked before creating it.
        Changing the test to 'if 1 or not hasattr'...
        is a handy way to temporarily recreate the attribute with a new value.
        """
        if 0 or not hasattr(self, 'circle_y'):
            self.circle_y = 100

    # If you want to change code inside an event handler
    # a simple wrapper as follows makes in 'hotswappable'.
    # The binding of _OnChar is not replaced by new versions
    # but OnChar is.
    def _OnChar(self, *args, **kwargs):
        self.OnChar(*args, **kwargs)

    def OnChar(self, event):
        print `event`
        # You may successively add code to explore the event
        # object further. Or you might read the documentation
        # and get everything right the first time.

        # print dir(event)

    def OnPaint(self, event):
        # If your program crashes on simple errors
        # like misspelled attributes, you should guard
        # critical methods like event handlers with a try block.
        try:
            dc = wx.PaintDC(self)
            self.DrawSomeFigures(dc)
        except Exception:
            import traceback
            traceback.print_exc()

        # Sometimes you can get away with a try-finally block
        # which might be even cleaner as well.
        # In OpenGL a typical error is a matrix stack overflow
        # because a pop operation is not reached due to a preceding
        # error. The idiom for cases like this is:
        # glPushMatrix()
        # try:
        #     ...
        # finally:
        #     glPopMatrix()

    def DrawSomeFigures(self, dc):
        self.init()
        # If you have hotswap running correctly, you may alter
        # coordinates and colors and see an immediate effect after
        # saving the source file.
        # You need not be too concerned about spelling mistakes
        # as this method is protected against runaway exceptions.
        dc.SetPen(wx.Pen(wx.BLUE, 3))
        dc.DrawLine(10, 10, 150, 150)
        dc.DrawCircle(self.circle_x, self.circle_y, 30)
        dc.SetPen(wx.Pen(wx.GREEN, 5))
        dc.DrawRectangle(self.circle_x + 60, 200, 30, 30)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    # Command line arguments of the script to be run are preserved by the
    # hotswap.py wrapper but hotswap.py and its options are removed that
    # sys.argv looks as if no wrapper was present.
    print "argv:", `argv`
    app = wx.PySimpleApp()
    f = TestFrame(None)
    f.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
