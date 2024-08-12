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
    "Mano De Raeve",
    "Siebe Lodewijckx",
    "Lander Carmans",
    "Justine Buteneers",
    "Ella Schepers",
    "Pieter Carmans",
    "Anna Kuppers",
    "An-Sofie Vandael",
    "Daan Leyssens",
    "Senne Bammens",
    "Liam Beckx",
    "Wout Lieten",
    "Oscar Vandercappellen",
    "Lyana Slegers",
    "Lies Bokken",
    "Ferre Kumbruck",
    "Robbe Geijsels",
    "Otto Vossen",
    "Robin Burnham",
    "Lou Moons",
    "Kobe Kumbruck",
    "Thaline Leys",
    "Eline Slegers",
    "Lore Bynens",
    "Tara Tutulic",
    "Kaen Clerix",
    "Stien Janssens",
    "Steegmans Anaïs",
    "Stef Zeelmaekers",
    "Anna Monten",
    "Daan Moesen",
    "Juul Tomassen",
    "Thibo Minten"])
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
    leidingslijst=list([
"Mano De Raeve",
"Siebe Lodewijckx",
"Lander Carmans",
"Justine Buteneers",
"Ella Schepers",
"Pieter Carmans",
"Anna Kuppers",
"An-Sofie Vandael",
"Daan Leyssens",
"Senne Bammens",
"Liam Beckx",
"Wout Lieten",
"Oscar Vandercappellen",
"Lyana Slegers",
"Lies Bokken",
"Ferre Kumbruck",
"Robbe Geijsels",
"Otto Vossen",
"Robin Burnham",
"Lou Moons",
"Kobe Kumbruck",
"Thaline Leys",
"Eline Slegers",
"Lore Bynens",
"Tara Tutulic",
"Kaen Clerix",
"Stien Janssens",
"Steegmans Anaïs",
"Stef Zeelmaekers",
"Anna Monten",
"Daan Moesen",
"Juul Tomassen",
"Thibo Minten"                      ])
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

  def output_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

    

    



