import wx, os, io

class theApp(wx.App):
    def __init__(self):
        super().__init__(redirect=False, clearSigInt=True)
        self.InitFrame()         
        
    def InitFrame(self):
            frame = theFrame(parent = None, title="The App", pos=(500, 300))
            frame.Show()
            
    
            
class theFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title = title, pos=pos)
        self.OnInit()
        self.create_toolbar()
        
    def OnInit(self):
        self.panel = thePanel(parent=self)

    def create_toolbar(self):
        self.toolbar = self.CreateToolBar()
        self.toolbar.SetToolBitmapSize((16,16))

        open_ico = wx.ArtProvider.GetBitmap(
            wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16,16))
        openTool = self.toolbar.AddTool(
            wx.ID_ANY, "Open", open_ico, "Open an Image Directory")
        self.Bind(wx.EVT_MENU, self.GetDir, openTool)

        self.toolbar.Realize()
    
    def GetDir(self, event):
        """
        Open a directory dialog
        """
        with wx.DirDialog(self, "Choose a directory",
                          style=wx.DD_DEFAULT_STYLE) as dlg:

            if dlg.ShowModal() == wx.ID_OK:
                self.pwd= dlg.GetPath()
                
                self.panel.photos = [f'{self.pwd}/{id}.png' for id in range(1,663,1)]
                photos = self.panel.photos
                if photos:
                    self.panel.update_photo(photos[0])
                    self.panel.total_photos = len(photos)
                else:
                    self.panel.reset()    

class thePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)
        self.max_size = 240
        self.photos = []
        self.current_photo = 1
        self.total_photos = 662
        self.layout()
    
    def layout(self):
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        img = wx.Image(self.max_size, self.max_size)
        self.image_ctrl = wx.StaticBitmap(self, wx.ID_ANY,
                                             wx.Bitmap(img))
        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL|wx.CENTER, 5)
        self.image_label = wx.StaticText(self, label="")
        self.main_sizer.Add(self.image_label, 0, wx.ALL|wx.CENTER, 5)

        btn_data = [("Previous", btn_sizer, self.on_previous),
                    ("Next", btn_sizer, self.on_next)]
        for data in btn_data:
            label, sizer, handler = data
            self.btn_builder(label, sizer, handler)

        self.main_sizer.Add(btn_sizer, 0, wx.CENTER)
        self.SetSizer(self.main_sizer)
    
    def btn_builder(self, label, sizer, handler):
        
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, handler)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
    
    def on_next(self, event):
        if not self.photos:
            return

        if self.current_photo == self.total_photos - 1:
            self.current_photo = 1
        else:
            self.current_photo += 1
        self.update_photo(self.photos[self.current_photo])
        print(self.photos)

    def on_previous(self, event):
        if not self.photos:
            return

        if self.current_photo == 1:
            self.current_photo = self.total_photos
        else:
            self.current_photo -= 1
        self.update_photo(self.photos[self.current_photo])
    
    def update_photo(self, image):
        img = wx.Image(image, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.max_size
            NewH = self.max_size * H / W
        else:
            NewH = self.max_size
            NewW = self.max_size * W / H
        img = img.Scale(NewW, NewH)

        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()
    
    def reset(self):
        img = wx.Image(self.max_size,
                       self.max_size)
        bmp = wx.Bitmap(img)
        self.image_ctrl.SetBitmap(bmp)
        self.current_photo = 0
        self.photos = []

if __name__=="__main__":
    app = theApp()
    app.MainLoop()
        