import random

slownik = {}
wykorzystane = []
umiem = []
nieumiem = []

while True:
    slowka = input('Wpisz wyrażenie do nauki: ')
    definicja = input('Wpisz tłumaczenie tego wyrażenia: ')
    nieumiem.append(slowka)
    slownik[f'{slowka}'] = [definicja]
    print(f'Oto twój słownik: {slownik}')
    zacznij = input('Jeśli chcesz przejść dalej napisz DALEJ, jeli chcesz kontynuować napisz cokolwiek. ')
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
    answer = input(f'Podaj znaczenie {question_key}: ')
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
        print(nieumiem)
        done = input(f"Oznaczyć pojęcie '{question_key}' jako opanowane? (Tak/Nie): ")
        done.upper()
        if done == "TAK":
            umiem.append(question_key)
            nieumiem.remove(question_key)
            print(nieumiem)
            if len(nieumiem) == 0:
                print('Brawo! Umiesz już wszystko!')
                continue_teching = input('Chcesz jeszcze raz się uczyć? (Tak/Nie)')
                continue_teching.upper()
                if continue_teching == 'TAK':
                    nieumiem.clear()
                    nieumiem.append(umiem)
                    umiem.clear()
                    continue
                else:
                    break
            else:
                continue
        else:
            nieumiem.append(question_key)
            continue
    else:
        print(f'Źle! Poprawna odpowiedź to {question_answer}')
        nieumiem.append(question_key)
        continue