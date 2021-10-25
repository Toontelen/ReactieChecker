from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run when the form opens.
    

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    
    
    
    
    
 
        
    

  def ButtonCheckLeiding_click(self, **event_args):
    leidingslijst=list(["Toon Telen", "Stan Schepers"])
    niet_gereageerd=list([])
    """This method is called when the button is clicked"""
    print("buttonclick")
    reacties=open(self.file_loader_1.file,"r")
    
    
    
    
    

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    



