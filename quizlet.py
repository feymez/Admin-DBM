import random

slownik = {}
wykorzystane = []
umiem = []
nieumiem = []

space = "===================="

while True:
    slowka = str(input('Wpisz wyrażenie do nauki: '))
    definicja = str(input('Wpisz tłumaczenie tego wyrażenia: '))
    nieumiem.append(slowka)
    slownik[f'{slowka}'] = [definicja]
    print(f'Oto twój słownik: {slownik}')
    zacznij = str(input('Jeśli chcesz przejść dalej napisz DALEJ, jeli chcesz kontynuować napisz cokolwiek. '))
    zacznij = zacznij.upper()
    if zacznij == 'DALEJ':
        break
    else:
        continue

def generate():
    global question_key, question_answer
    while True:
            question_key = random.choice(list(slownik.keys()))
            question_answer = slownik.get(f'{question_key}')
            question_answer = str(question_answer)
            question_answer = question_answer.replace("['", "")
            question_answer = question_answer.replace("']", "")
            if question_key in wykorzystane:
                continue
            elif question_key in umiem:
                continue
            else:
                break

while True:
    generate()
    answer = str(input(f'Podaj znaczenie {question_key}: '))
    if answer == question_answer:
        print('Dobra odpowiedź!')
        wykorzystane.append(question_key)
        """slownik_keys = str(slownik.keys())
        slownik_keys = slownik_keys.replace("dict_keys(['", "")
        slownik_keys = slownik_keys.replace("'])", "")
        slownik_keys = slownik_keys.replace("', '", " ")
        nieumiem = nieumiem.append(slownik_keys)
        wykorzystane_ = str(wykorzystane)
        wykorzystane_ = wykorzystane_.replace("['", "")
        wykorzystane_ = wykorzystane_.replace("']", "")
        wykorzystane_ = wykorzystane_.replace("', '", "")
        """
        print(f'Lista nieumiem: {nieumiem}')
        print(f'Lista umiem: {umiem}')
        while True:
            done = str(input(f"Oznaczyć pojęcie '{question_key}' jako opanowane? (Tak/Nie): "))
            done = done.upper()
            if done == "TAK":
                print(space)
                print(f"Wyrażenie '{question_key}' zostało oznaczone jako opanowane.")
                while True:
                    sure = str(input("Czy na pewno powinno zostać oznaczone? (Tak/Nie): "))
                    sure = sure.upper()
                    if sure == "TAK":
                        umiem.append(question_key)
                        nieumiem.remove(question_key)
                        break
                    elif sure == "NIE":
                        print(f"Wyrażenie '{question_key}' zostało odznaczone")
                        break
                    else:
                        continue
                print(space)
                if len(nieumiem) == 0:
                    while True:
                        continue_teachning = str(input('Chcesz uczyć się dalej? (Tak/Nie): '))
                        continue_teachning = continue_teachning.upper()
                        if continue_teachning == "TAK":
                            nieumiem.clear()
                            nieumiem.append(umiem)
                            umiem.clear()
                            break
                        elif continue_teachning == "NIE":
                            print('Powodzenia! Żegnam!')
                            break
                        else:
                            continue
                else:
                    continue
            elif done == "NIE":
                print(f"Wyrażenie '{question_key}' nie zostało oznaczone")
                while True:
                    sure = str(input("Czy na pewno nie powinno zostać oznaczone? (Tak/Nie): "))
                    sure = sure.upper()
                    if sure == "TAK":
                        print(space)
                        print(f"Wyrażenie '{question_key}' nie zostało oznaczone")
                        break
                    elif sure == "NIE":
                        print(space)
                        print(f"Wyrażenie '{question_key}' zostało oznaczone")
                        umiem.append(question_key)
                        nieumiem.remove(question_key)
                        break
                    else:
                        continue
                print(space)
                if len(nieumiem) == 0:
                    while True:
                        continue_teachning = str(input('Chcesz uczyć się dalej? (Tak/Nie): '))
                        continue_teachning = continue_teachning.upper()
                        if continue_teachning == "TAK":
                            nieumiem.clear()
                            nieumiem.append(umiem)
                            umiem.clear()
                            break
                        elif continue_teachning == "NIE":
                            print('Powodzenia! Żegnam!')
                            break
                        else:
                            continue
                else:
                    continue
                print('Break na NIE')
                break
            else:
                print("Else")
                continue
    else:
        print(f'Źle! Poprawna odpowiedź to {question_answer}')
        if question_key not in nieumiem:
            nieumiem.append(question_key)
        else:
            continue