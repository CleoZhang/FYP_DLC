import wx
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(350,200))
app = wx.App(redirect=True)
top = Frame("Hello World")
top.Show()
app.MainLoop()

