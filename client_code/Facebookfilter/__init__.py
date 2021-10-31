from ._anvil_designer import FacebookfilterTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Facebookfilter(FacebookfilterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run when the form opens.
    

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    
    
    
    
    
 
        
    

  def ButtonCheckLeiding_click(self, **event_args):
    leidingslijst=list(["Kobe Lobbinger",
"Ward Borghoms",
"Joris Ganne",
"Keanu Reekmans",
"Daan Vaes",
"Klaas Coninx",
"Sien Telen",
"Anna Vandercappellen",
"Stan Schepers",
"Lore Vanrijckeghem",
"Seppe Vaes",
"Tom Maddelein",
"Frederik Vandael",
"Merle Daniels",
"Janne Achten",
"Jonas Snellings",
"Toon Telen",
"Simon Ganne",
"Nico Nilis",
"Jeroen Steegmans",
"Ken Vanoosterhout",
"Liam Reekmans",
"Kay Vanbaelen",
"Briek Moons",
"Thibauld Buteneers",
"Youlian Burnham",
"Lander Carmans",
"Fien Bokken",
"Flore Vandercappellen",
"Daan Vanreppelen",
"Sara Franssens",
"Ranya Kitsinis",
"Lorien Zeelmaekers",
"Nikola Juszczak",
"Ellen Franssens",
"Nore Daniels",
"Jan Vanrijckeghem",
"Britt Kumbruck",
"Lara Kumbruck",
"Senne Bammens",
"Ella Schepers",
"An-Sofie Vandael",
"Bram Vaes",
"Siebe Lodewijckx",
"Ian Vanoosterhout",
"Cel Sterkens",
"Emily Kolpers",
"Flore Nys",
"Lies Bokken",
"Lola Moons",
"Tibo Leyssens"])
    niet_gereageerd=list([])
    """This method is called when the button is clicked"""
    print("buttonclick")
    reacties= self.text_area_1.text
#     reacties2= self.text_box_1.text
    
    afwezig_string=""
    afwezig_lijst=list([])
    for leiding in leidingslijst:
       if leiding not in reacties:
        afwezig_lijst.append(leiding)
        afwezig_string+="\n" + leiding
        
    
    
    self.output.text=" "+ afwezig_string
    self.text_box_1.text= (f"Er moet nog {len(afwezig_lijst)} leiding reageren:")
    

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    



