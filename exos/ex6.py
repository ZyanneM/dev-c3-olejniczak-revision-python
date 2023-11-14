from datetime import datetime
import locale

def getDateTime():
    locale.setlocale(locale.LC_TIME, "fr_FR")
    now = datetime.now()
    formatted_date = now.strftime("%A %d %B %Y %H:%M:%S")

    print("La date et l'heure actuelles sont : ", formatted_date)

getDateTime()