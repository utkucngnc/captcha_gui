import wx, os

class theApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.InitFrame()         
        
    def InitFrame(self):
            frame = theFrame(parent = None, title="The App", pos=(300, 200))
            frame.Show()
            
    
            
class theFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title = title, pos=pos)
        self.OnInit()
        
    def OnInit(self):
        panel = thePanel(parent=self)
        #button = wx.Button(panel, label = "Browse", pos=(130,10), size =(60,20))
        #self.Bind(wx.EVT_BUTTON, , button)
        

class thePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)
        self.GetDir() 
        
        wtxt = wx.StaticText(self, id = wx.ID_ANY, label = self.pwd, pos=(20,20))
    
    def GetDir(self):
        dlg = wx.DirDialog (None, "Choose input directory", "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.pwd = dlg.GetPath()
        else:
            self.pwd = os.getcwd()  
        


if __name__=="__main__":
    app = theApp()
    app.MainLoop()
        