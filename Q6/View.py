import wx

"""
    Defines the GUI elements for the program using wxPython
"""

class View(wx.Frame):

    def __init__(self):

        # Class Initialiser

        frame = wx.Frame.__init__(self, None, -1,"City Information", pos = (700,300), size = (500,500), name = "frame")
        panel = self.panel = wx.Panel(self, wx.ID_ANY)
        self.total_list = wx.ComboBox(self.panel, wx.ID_ANY, "Enter City Name",size = (200,-1))

        # Set the default values to be displayed before user city selection and the style type for the output fields

        self.displayElements_list = list();
        self.displayElement_countyname = wx.TextCtrl(self.panel, wx.ID_ANY, "County Name", style=wx.TE_READONLY | wx.TE_CENTER)
        self.displayElement_latitude = wx.TextCtrl(self.panel, wx.ID_ANY, "Latitude Value", style=wx.TE_READONLY | wx.TE_CENTER)
        self.displayElement_longitude = wx.TextCtrl(self.panel, wx.ID_ANY, "Longitude Value", style=wx.TE_READONLY | wx.TE_CENTER)

        # Put them in a list for easier reference

        self.displayElements_list = [self.displayElement_countyname,self.displayElement_latitude,self.displayElement_longitude]
        self.Set_frame()

    def Set_frame(self):

        # Frame Initialiser

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        output_fields = [("City", self.total_list),("County", self.displayElements_list[0]),("Latitude", self.displayElements_list[1]),("Longitude", self.displayElements_list[2])]

        for display_fieldtype, display_output in output_fields:
            default = wx.StaticText(self.panel, -1, display_fieldtype , size=(100, -1))
            set_width = wx.BoxSizer(wx.HORIZONTAL)
            set_width.Add(default, 0, wx.ALL, 4)
            set_width.Add(display_output, 1, wx.ALL | wx.EXPAND, 4)
            self.sizer.Add(set_width, 0, wx.ALL | wx.EXPAND, 4)

        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)