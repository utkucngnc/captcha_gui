import wx

class theApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()
        #self.
        
    def InitFrame(self):
            frame = theFrame(parent = None, title="The App", pos=(100, 100))
            frame.Show()
            
class theFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title = title, pos=pos)
        self.OnInit()
        
    def OnInit(self):
        panel = thePanel(parent=self)

class thePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)


if __name__=="__main__":
    app = theApp()
    app.MainLoop()
        