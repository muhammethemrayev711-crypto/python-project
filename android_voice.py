# -*- coding: utf-8 -*-

from jnius import autoclass
from android import activity



PythonActivity = autoclass(
    "org.kivy.android.PythonActivity"
)


SpeechRecognizer = autoclass(
    "android.speech.SpeechRecognizer"
)


RecognizerIntent = autoclass(
    "android.speech.RecognizerIntent"
)


class VoiceListener:


    def __init__(self, callback):


        self.callback = callback


        self.activity = PythonActivity.mActivity


        self.recognizer = SpeechRecognizer.createSpeechRecognizer(
            self.activity
        )



        self.listener = VoiceRecognitionListener(
            self.callback
        )


        self.recognizer.setRecognitionListener(
            self.listener
        )







    def start(self):


        intent = autoclass(
            "android.content.Intent"
        )()



        intent.setAction(

            RecognizerIntent.ACTION_RECOGNIZE_SPEECH

        )



        intent.putExtra(

            RecognizerIntent.EXTRA_LANGUAGE,

            "tr-TR"

        )



        intent.putExtra(

            RecognizerIntent.EXTRA_LANGUAGE_MODEL,

            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM

        )



        self.recognizer.startListening(

            intent

        )









class VoiceRecognitionListener:


    def __init__(self,callback):

        self.callback = callback





    def onResults(self,bundle):


        results = bundle.getStringArrayList(

            SpeechRecognizer.RESULTS_RECOGNITION

        )


        if results:


            self.callback(

                results.get(0)

            )







    def onError(self,error):

        pass



    def onReadyForSpeech(self,params):

        pass


    def onBeginningOfSpeech(self):

        pass


    def onRmsChanged(self,value):

        pass


    def onBufferReceived(self,buffer):

        pass


    def onEndOfSpeech(self):

        pass


    def onPartialResults(self,partial):

        pass


    def onEvent(self,event,params):

        pass