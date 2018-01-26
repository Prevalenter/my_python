import wx
from moudle import *
from Granule import show_Granule
from Analysis import show_analysis
from Connected import show_Connected
    
class MainWindow(wx.Frame):
    def __init__(self, parent,title,size):
        wx.Frame.__init__(self,parent,title=title,pos=wx.DefaultPosition,size=size)
        filemenu= wx.Menu()
        menuAnalysis = filemenu.Append(wx.ID_FILE1, "show cell Analysis:")
        menuConnected= filemenu.Append(wx.ID_FILE2, "show cell Connected")
        menuGranule = filemenu.Append(wx.ID_FILE3,"show cell with Granule")
        menuExit = filemenu.Append(wx.ID_EXIT,"Exit")
                                       
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&show")
        self.SetMenuBar(menuBar)
        # Events.
        self.Bind(wx.EVT_MENU, self.OnAnalysis, menuAnalysis)
        self.Bind(wx.EVT_MENU, self.OnConnected, menuConnected)
        self.Bind(wx.EVT_MENU, self.OnGranule, menuGranule)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

#        panel =ExamplePanel(self)
    def OnAnalysis(self,e):
        print(1)
        fig1=plt.figure('show')
        img1=imread('1.png',True)
        img2 =np.zeros_like(img1).astype(np.int16)
        img2=show_analysis(img1)
        
        plt.subplot(121)
        plt.imshow(img1,cmap='gray')
        plt.subplot(122)
        plt.imshow(img2)
        plt.show()
    def OnConnected(self,e):
        print(2)
        show_Connected()
    def OnGranule(self,e):
        print(3)
        show_Granule()
    def onTestMe(self,event):
        frame1=TestFrame()
        frame1.Show()
    def onCloseWindow(self,event):
        self.Destroy()
    def OnExit(self,e):
        self.Close(True)
        
if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow(None,'无碳小车调试助手V1')
    frame.Show()
    app.MainLoop()
