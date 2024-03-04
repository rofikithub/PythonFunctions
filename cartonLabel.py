from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
import requests
from pathlib import Path

kv = """
ScreenManager:
    Screen:
        MDTextField:
            id: article
            hint_text: "ARTICLE NO"
            pos_hint: {"center_x": 0.3, "center_y": 0.9}
            size_hint_x: 0.3
        MDTextField:
            id: color
            hint_text: "COLOR"
            pos_hint: {"center_x": 0.7, "center_y": 0.9}
            size_hint_x: 0.3
        MDTextField:
            id: size
            hint_text: "SIZE"
            pos_hint: {"center_x": 0.3, "center_y": 0.8}
            size_hint_x: 0.3
        MDTextField:
            id: quantity
            hint_text: "QUANTITY OF PCS"
            pos_hint: {"center_x": 0.7, "center_y": 0.8}
            size_hint_x: 0.3
        MDTextField:
            id: order
            hint_text: "ORDER"
            pos_hint: {"center_x": 0.3, "center_y": 0.7}
            size_hint_x: 0.3
        MDTextField:
            id: gross
            hint_text: "GROSS WT (KG)"
            pos_hint: {"center_x": 0.7, "center_y": 0.6}
            size_hint_x: 0.3
        MDTextField:
            id: netwt
            hint_text: "NET WT (KG)"
            pos_hint: {"center_x": 0.3, "center_y": 0.6}
            size_hint_x: 0.3
        MDTextField:
            id: start
            hint_text: "START CARTON NO"
            pos_hint: {"center_x": 0.3, "center_y": 0.5}
            size_hint_x: 0.3
        MDTextField:
            id: end
            hint_text: "END CARTON NO"
            size_hint_x: 0.3
            pos_hint:{'center_x': 0.7, 'center_y': 0.5}
        
        MDFlatButton:
            text: "Click"
            on_press:app.download_xml_file('obj')
            md_bg_color:app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.3}
  
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Orange"
        screen = Screen()
        self.string = Builder.load_string(kv)
        screen.add_widget(self.string)
        return screen


    def download_xml_file(self,obj):
            content = '<?xml version="1.0" encoding="utf-8"?>\n<Kartonetiketten xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:de.ttg:intex:kartonetiketten:2014-09-04">'
            article  = int(self.string.ids.article.text)
            color    = int(self.string.ids.color.text)
            size     = str(self.string.ids.size.text)
            quantity = int(self.string.ids.quantity.text)
            order = int(self.string.ids.order.text)
            gross = int(self.string.ids.gross.text)
            netwt = int(self.string.ids.netwt.text)
            start = int(self.string.ids.start.text)
            end   = int(self.string.ids.end.text)
            for x in range(start, end+1):
                xml = (''
                    '<Etikett bestellnr="450065704">\n'
                        '<artsnr>'+str(size)+'</artsnr>\n'
                        '<artikelbez>softshell jacket, sky captain blue, S</artikelbez>\n'
                        '<soko>00</soko>\n'
                        '<produktlinie>10</produktlinie>\n'
                        '<farbe>'+str(color)+'</farbe>\n'
                        '<saison>407</saison>\n'
                        '<kollektion>O</kollektion>\n'
                        '<eancode>4067672649728</eancode>\n'
                        '<size sizebez="'+str(size)+'" />\n'
                        '<quantityOfPieces>'+str(quantity)+'</quantityOfPieces>\n'
                        '<specialMarking>E Shop</specialMarking>\n'
                        '<specialMarkingShort>@</specialMarkingShort>\n'
                        '<grossWt>'+str(gross)+'</grossWt>\n'
                        '<netWt>'+str(netwt)+'</netWt>\n'
                        '<cartonNo>'+str(x)+'</cartonNo>\n'
                    '</Etikett>\n'
                      )
                content = content + xml
                content = content + '\n</Kartonetiketten>'

            with open('datafile.xml', 'w') as file:
                file.write(content)


DemoApp().run()
