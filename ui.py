# -*- coding: utf-8 -*-

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


from android_voice import VoiceListener
from music_scan import tarama_yap, sarki_bul
from music_player import muzik_ac




class MusicButton(Button):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.background_normal = ""

        self.background_color = (
            0.85,
            0.65,
            0.1,
            1
        )


        self.color = (
            0,
            0,
            0,
            1
        )






class MusicPanel(FloatLayout):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)



        self.dinliyor = False

        self.voice = None





        # MP3 listesini hazırla

        try:

            tarama_yap()

        except:

            pass






        self.start = MusicButton(

            text="START",

            font_size=25,

            size_hint=(None,None),

            size=(220,60),

            pos=(40,420)

        )


        self.start.bind(

            on_release=self.baslat

        )


        self.add_widget(self.start)







        self.info = Label(

            text="Hazır",

            font_size=18,

            size_hint=(None,None),

            size=(280,100),

            pos=(10,250)

        )


        self.add_widget(self.info)









    def baslat(self,button):


        if self.dinliyor:


            self.dinliyor=False


            button.text="START"


            self.info.text="Dinleme kapandı"



        else:


            self.dinliyor=True


            button.text="STOP"


            self.info.text="Seni dinliyorum..."



            self.voice = VoiceListener(

                self.ses_geldi

            )


            self.voice.start()







    def ses_geldi(self,text):


        self.info.text = text



        # şarkıyı ara


        sonuc = sarki_bul(text)



        if sonuc:


            self.info.text = (

                "Açılıyor:\n"

                + sonuc

            )



            muzik_ac(

                sonuc

            )



        else:


            self.info.text = (

                "Şarkı bulunamadı"

            )