def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print('\n--- Telefon daftari ---')
        print('1. Kontakt qo‘shish')
        print('2. Barcha kontaktlarni chiqarish')
        print('3. Ism bo‘yicha telefon qidirish')
        print('0. Chiqish')

        choice = input('Tanlang (0-3): ')

        if choice == '1':
            name = input('Ismni kiriting: ')
            phone = input('Telefon raqamini kiriting: ')
            phonebook[name] = phone
            print('Kontakt qo‘shildi.')

        elif choice == '2':
            if not phonebook:
                print('Telefon daftari bo‘sh.')
            else:
                for name, phone in phonebook.items():
                    print(name, '->', phone)

        elif choice == '3':
            name = input('Qidirilayotgan ismni kiriting: ')
            if name in phonebook:
                print(name, '->', phonebook[name])
            else:
                print('Bunday kontakt topilmadi.')

        elif choice == '0':
            print('Dastur tugadi.')
            break

        else:
            print('Noto‘g‘ri tanlov!')

            
phonebook = {}
phonebook_menu(phonebook)
