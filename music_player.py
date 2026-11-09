# -*- coding: utf-8 -*-

from jnius import autoclass



PythonActivity = autoclass(
    "org.kivy.android.PythonActivity"
)


Intent = autoclass(
    "android.content.Intent"
)


Uri = autoclass(
    "android.net.Uri"
)





def muzik_ac(yol):


    try:


        activity = PythonActivity.mActivity



        dosya = Uri.parse(

            "file://" + yol

        )



        intent = Intent(

            Intent.ACTION_VIEW

        )


        intent.setDataAndType(

            dosya,

            "audio/*"

        )


        intent.addFlags(

            Intent.FLAG_ACTIVITY_NEW_TASK

        )


        activity.startActivity(

            intent

        )



        return True



    except Exception as e:


        print(e)


        return False