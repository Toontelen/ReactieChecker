from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.check_lijst()

    # Any code you write here will run when the form opens.
    

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    tekst=self.text_area_1.text
    
  def check_lijst(self):
    tekst=self.text_area_1.text
    leidingslijst=list(['Toon Telen', 'Ken Vanoosterhout','Stan Schepers'])
    for leiding in leidingslijst:
      if leiding in tekst: 
        print(leiding, 'zit in de tekst')
        
    

