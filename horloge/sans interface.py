import time
def temps():
    heures = int(input("heures : "))
    minutes = int(input("minutes : "))
    secondes = int(input("secondes : "))

    alarmeh = int(input("alarme h : "))
    alarmem = int(input("alarme m : "))
    alarmes = int(input("alarme s : "))

    while heures<24:
        while minutes<60:
            while secondes<60:
                if alarmeh == heures:
                    if alarmem == minutes:
                        if alarmes == secondes:
                            print("debout")

                print(heures,':',minutes,':',secondes)
                time.sleep(1)
                secondes=secondes+1
            secondes=0
            minutes=minutes+1
    heures=heures+1
    minutes=0

temps()