import sys
import logging
import datetime as dt
import time

file_name = f"{dt.datetime.today().day}_{dt.datetime.today().month}_{dt.datetime.today().year}"

# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s',
#                     filename = f"{file_name}.log")

logging.basicConfig(level=logging.INFO,
    format='%(message)s')

def input_as_number(liczba):
    if ("." in liczba):
        liczba = float(liczba)
    elif ("," in liczba):
        liczba = float(liczba.replace(",","."))
    else:
        liczba = int(liczba)
    return liczba

def main():
    
    dzialanie = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    
    if dzialanie == '1':
        print("Możesz podać 2 składniki lub więcej.")
        wynik = 0
        skladniki = []
        i = 0
        while True:
            i += 1
            if i <= 2:
                liczba = input(f'Podaj składnik nr {i}: ')
            else:
                liczba = input(f'Podaj składnik nr {i} lub naciśnij Enter: ')
            if liczba != '':
                if liczba.isalpha():
                    logging.warning("Podana wartość nie jest liczbą!")
                    i -= 1
                    continue
                liczba = input_as_number(liczba)
                skladniki.append(liczba)
                logging.info(f"Podano liczbę {liczba}")
                wynik += liczba
                wynik = int(wynik) if wynik % 1 == 0 else wynik
            else:
                if len(skladniki) > 2:
                    message = ', '.join([str(j) for j in skladniki])
                elif len(skladniki) == 2:
                    message = f'{skladniki[0]} oraz {skladniki[1]}'
                logging.info(f"Dodaję liczby: {message}.")
                logging.info(f'Wynik dodawania to: {wynik}.')
                # time.sleep(5)
                break
    
    elif dzialanie == '2':
        print("Możesz podać 2 liczby.")
        while True:
            liczba_1 = input('Podaj liczbę nr 1: ')
            if liczba_1.isalpha():
                logging.warning("Podana wartość nie jest liczbą!")
                continue
            else:
                liczba_1 = input_as_number(liczba_1)
                break
        while True:
            liczba_2 = input('Podaj liczbę nr 2: ')
            if liczba_2.isalpha():
                logging.warning("Podana wartość nie jest liczbą!")
                continue
            else:
                liczba_2 = input_as_number(liczba_2)
                break
        wynik = liczba_1-liczba_2
        wynik = int(wynik) if wynik % 1 == 0 else wynik
        logging.info(f"Odejmuję liczby: {liczba_1} i {liczba_2}.")
        logging.info(f'Wynik dodawania to: {wynik}.')
        # time.sleep(5)
        
    elif dzialanie == '3':
        print("Możesz podać 2 czynniki lub więcej.")
        wynik = 1
        czynniki = []
        i = 0
        while True:
            i += 1
            if i <= 2:
                liczba = input(f'Podaj czynnik nr {i}: ')
            else:
                liczba = input(f'Podaj czynnik nr {i} lub naciśnij Enter: ')
            if liczba != '':
                if liczba.isalpha():
                    logging.warning("Podana wartość nie jest liczbą!")
                    i -= 1
                    continue
                liczba = input_as_number(liczba)
                czynniki.append(liczba)
                logging.info(f"Podano liczbę {liczba}")
                wynik *= liczba
                wynik = int(wynik) if wynik % 1 == 0 else wynik
            else:
                if len(czynniki) > 2:
                    message = ', '.join([str(j) for j in czynniki])
                elif len(czynniki) == 2:
                    message = f'{czynniki[0]} oraz {czynniki[1]}'
                logging.info(f"Mnożę liczby: {message}.")
                logging.info(f'Wynik mnożenia to: {wynik}.')
                # time.sleep(5)
                break    

    elif dzialanie == '4':
        print("Możesz podać 2 liczby.")
        while True:
            liczba_1 = input('Podaj liczbę nr 1: ')
            if liczba_1.isalpha():
                logging.warning("Podana wartość nie jest liczbą!")
                continue
            else:
                liczba_1 = input_as_number(liczba_1)
                break
        while True:
            liczba_2 = input('Podaj liczbę nr 2: ')
            if liczba_2.isalpha():
                logging.warning("Podana wartość nie jest liczbą!")
                continue
            elif input_as_number(liczba_2) == 0:
                logging.warning("Dzielenie przez zero jest niedozwolone!")
                continue
            else:
                liczba_2 = input_as_number(liczba_2)
                break
        wynik = liczba_1/liczba_2
        wynik = int(wynik) if wynik % 1 == 0 else wynik
        logging.info(f"Dzielę liczby: {liczba_1} i {liczba_2}.")
        logging.info(f'Wynik dzielenia to: {wynik}.')
    
    else:
        logging.warning("Nie wybrałeś żadnego z dostępnych działań.")
    
    input('By zakończyć naciśnij Enter.')

if __name__ == '__main__':
    # pass
    main()
# sys.exit()
