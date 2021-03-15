import pyfiglet
from functions import *




while True:
    print("""
    1) Zip
    2) Unzip
    99) Exit       
    """)

    option = input('>>')

    if option == '1':
        while True:
            file = input('Enter file name or path: ')
            find_files(file)

            if len(result) == 1:
                zip(result[0])
                break
            else:
                if len(result) > 1:
                    print('There are too many files with this name.')
                    n = 0
                    for file in result:
                        print(f'{n}) {result[n]}')
                        n += 1
                    file = int(input('Enter file number: '))
                    zip(result[file])
                    break
    if option == '2':
        while True:
            file = input('Enter file name or path: ')
            find_files(file)

            if len(result) == 1:
                unzip(result[0])
                break
            else:
                if len(result) > 1:
                    print('There are too many files with this name.')
                    n = 0
                    for file in result:
                        print(f'{n}) {result[n]}')
                        n += 1
                    file = int(input('Enter file number: '))
                    unzip(result[file])
                    break




    if option == '99':
        exit()

