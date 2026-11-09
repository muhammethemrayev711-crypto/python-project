# -*- coding: utf-8 -*-

import os
import json



KAYIT_DOSYASI = "mp3_list.json"



ARAMA_KLASORLERI = [

    "/storage/emulated/0/Music",

    "/storage/emulated/0/Download",

    "/storage/emulated/0"

]





def mp3leri_tara():


    liste = []


    for klasor in ARAMA_KLASORLERI:


        if os.path.exists(klasor):


            for root, dirs, files in os.walk(klasor):


                for dosya in files:


                    if dosya.lower().endswith(".mp3"):


                        yol = os.path.join(

                            root,

                            dosya

                        )


                        liste.append(yol)




    return liste







def kaydet(liste):


    with open(

        KAYIT_DOSYASI,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            liste,

            f,

            ensure_ascii=False,

            indent=4

        )








def yukle():


    try:


        with open(

            KAYIT_DOSYASI,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)



    except:


        return []









def tarama_yap():


    liste = mp3leri_tara()


    kaydet(liste)


    return liste










def sarki_bul(kelime):


    kelime = kelime.lower()


    liste = yukle()



    for sarki in liste:


        isim = os.path.basename(

            sarki

        ).lower()



        if kelime in isim:


            return sarki





    return None