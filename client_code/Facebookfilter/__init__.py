from ._anvil_designer import FacebookfilterTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import re
# import pandas as pd
# from Facebookfilter import Facebookfilter

class Facebookfilter(FacebookfilterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run when the form opens.
    

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    
    
#   def link_1_click(self, **event_args):
#     """This method is called when the link is clicked"""
#     self.content_panel.clear()
#     self.content_panel.add_component(Form2())
     
    
 
    

  def ButtonCheckLeiding_click(self, **event_args):
    leidingslijst=list([
"Frederik Vandael",
"Jonas Snellings",
"Toon Telen",
"Jeroen Steegmans",
"Ken Vanoosterhout",
"Lander Carmans",
"Fien Bokken",
"Flore Vandercappellen",
"Sara Franssens",
"Nikola Juszczak",
"Senne Bammens",
"Ella Schepers",
"An-Sofie Vandael",
"Siebe Lodewijckx",
"Cel Sterkens",
"Lies Bokken",
"Pieter Carmans",
"Ferre Kumbruck",
"Thibo Minten", 
"Mano De Raeve",
"Liam Beckx",
"Anna Kuppers",
"Rik Van Avermaet",
"Robbe Geijsels",
"Lyana Slegers",
"Wout Lieten",
"Oscar Vandercappellen",
"Justine Buteneers",
"Daan Leyssens"])
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

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    # self.content_panel.clear()
    # self.content_panel.add_component(teller())
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    leidingslijst=list(["Kobe Lobbinger",
"Sien Telen",
"Anna Vandercappellen",
"Stan Schepers",
"Frederik Vandael",
"Merle Daniels",
"Jonas Snellings",
"Toon Telen",
"Jeroen Steegmans",
"Ken Vanoosterhout",
"Liam Reekmans",
"Kay Vanbaelen",
"Briek Moons",
"Thibauld Buteneers",
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
"Siebe Lodewijckx",
"Ian Vanoosterhout",
"Cel Sterkens",
"Flore Nys",
"Lies Bokken",
"Lola Moons",
"Tibo Leyssens",
"Nele Ganne",
"Arno Vanrijckeghem",
"Otto Vossen",
"Pieter Carmans",
"Matteo Michetti",
"Sam Gielen", 
"Ferre Kumbruck",
"Thibo Minten", 
"Mano De Raeve",
"Axel Tielens",
"Robin Burnham",
"Liam Beckx",
"Anna Kuppers"])
    leidingslijst2=list() 
    for leider in leidingslijst:
      leider=leider.strip()
      # leider=leider.lower()
      leidingslijst2.append(leider)
    reacties= self.text_area_1.text
    score_dict=dict()
    sortedDict=dict()
    tekst=[]
    for index, zin in enumerate(reacties):
      # zin=zin.lower()
      zin=zin.strip()
      tekst.append(zin)

    for i, t in enumerate(tekst):
    #     print(i,t)
        match = re.search('aanwezig', t)
        if match:
            print("we hebben een match!")
            if tekst[i-1] in leidingslijst2:
    #             print("leiding gevonden:", tekst[i-1])
                score_dict[tekst[i-1]]=+1  
            elif tekst[i-2] in leidingslijst2:
    #             print("leiding gevonden:", tekst[i-2])
                score_dict[tekst[i-2]]=+1 
            elif tekst[i-3] in leidingslijst2:
    #             print("leiding gevonden:", tekst[i-3])
                score_dict[tekst[i-3]]=+1 
            
    for leiding in leidingslijst2:
        if leiding not in score_dict.keys():
            print(leiding, "niet gevonden!")
            score_dict[leiding]=0
        
    sortedDict = dict(sorted(score_dict.items(), key=lambda x: x[0].lower()) )
        
    for k,v in sortedDict.items():
      self.output.text=('{}: {}'.format(k,v))
        
    aantal_aanwezig=len(sortedDict.items())
    print("aantal leiding aanwezig:",aantal_aanwezig)
    
    # print(sortedDict.keys())
    # self.output.text=sortedDict.items()
    self.text_box_1.text= (f"Er is {len(sortedDict.keys())} leiding afwezig")
    self.output.text=sortedDict.items()

    

    



