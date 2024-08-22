from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from bs4 import BeautifulSoup
import requests

username_helper = '''
MDTextField:
    hint_text: 'Area'
    pos_hint: {'center_x':0.5,'center_y':0.94}
    size_hint_x: None
    width:300
'''

class Weather_Conditions_PrakEnTechApp(MDApp):
    def show(self, obj, add_widget=MDLabel):
        screen = Screen()
        area1 = self.textfield.text
        r = requests.get('https://www.google.com/search?sxsrf='+
                         'ALeKk001t27n2Ott-CxnbmlcfPOXXNuLPA%3A1593587990124&source=hp&ei=Fjn8XvDVBamc4-EPtdKG4Aw&q=temperature+in+'+area1)
        soup = BeautifulSoup(r.text,'lxml')
        c = 0
        for A_Tag in soup.select('div[class*="BNeawe iBp4i AP7Wnd"]') :
            if c==1:
                break
            Degree = A_Tag.get_text()
            c+=1
        c = 0    
        for A_Tag in soup.select('div[class*="BNeawe tAd8D AP7Wnd"]') :
            if c==1:
                break
            Details = A_Tag.get_text()
            c+=1
        self.label.text = Details+'\n'+Degree
        return self.label.text
    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        self.textfield = Builder.load_string(username_helper)
        screen.add_widget(self.textfield)
        flt_btn = MDRectangleFlatButton(on_release = self.show, text = 'CHECK',pos_hint = {'center_x':0.5,'center_y':0.05})
        screen.add_widget(flt_btn)
        self.label = MDLabel(text='', halign='center', theme_text_color = "Custom",text_color=(255/255.0,225/255.0,0,1), font_style='H5')
        screen.add_widget(self.label)
        return screen
Weather_Conditions_PrakEnTechApp().run()
