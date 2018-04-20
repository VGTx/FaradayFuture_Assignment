import json
import wx
from Model import Model_Data
from View import View

"""
    Controls the overall interaction between the Model and the View components of the 
    program
"""
class Controller(object):

    def __init__(self):

    # Controller Initialiser
    # Loads objects from Model and View classes and defines their interactions

        self.app = wx.App()
        self.model = Model_Data()
        self.view = View()
        self.view.total_list.AppendItems(self.model.Get_List())
        self.view.Bind(wx.EVT_COMBOBOX, self.Search_city)

    def Search_city(self, event):

    # Display data corresponding to selected city

        selection = self.view.total_list.GetValue()
        to_display = self.model.Return_Data(selection)
        current_data = [(self.view.displayElement_countyname, to_display[0]),(self.view.displayElement_latitude, to_display[1]),(self.view.displayElement_longitude, to_display[2])]
        i = 0
        for element in self.view.displayElements_list:
            self.view.displayElements_list[i].Clear()
            self.view.displayElements_list[i].write(to_display[i])
            i += 1

    def Launch_app(self):

        self.view.Show()
        self.app.MainLoop()

