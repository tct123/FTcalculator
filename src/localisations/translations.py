import os
from mylocale import tr
from flet_localisation import locale
import flet as ft


trfile = f"{os.path.dirname(__file__)}/localisation.csv"


def HELLOMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="HELLOWORLD",
        langcode=langcode,
    )


def MENUEHINTMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="SHOWMENUEHINT",
        langcode=langcode,
    )


def TITLE(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="TITLE",
        langcode=langcode,
    )


def DATAPROTECTIONITEM(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="DATAPROTECTIONITEM",
        langcode=langcode,
    )
