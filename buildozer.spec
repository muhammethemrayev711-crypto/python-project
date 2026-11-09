[app]

# Uygulama adı
title = Music Assistant


# Paket adı
package.name = musicassistant


# Paket domain
package.domain = org.muhammet


# Ana dosya
source.main = main.py


# Dosya uzantıları
source.include_exts = py,png,jpg,kv,json


# Python ve Kivy
requirements = python3,kivy,pyjnius


# Ekran yönü
orientation = portrait



# Android izinleri
android.permissions = RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE



# Android API

android.api = 29

android.minapi = 23



# Android mimari

android.archs = arm64-v8a,armeabi-v7a



# Uygulama versiyonu

version = 0.1



# Log

android.logcat_filters = *:S python:D