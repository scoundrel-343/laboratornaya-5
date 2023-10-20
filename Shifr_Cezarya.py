# Функция для шифрования
def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                encrypted_char = chr((ord(letter) - ord('А') + shift) % 32 + ord('А'))
            else:
                encrypted_char = chr((ord(letter) - ord('а') + shift) % 32 + ord('а'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += letter
    return encrypted_text

# Функция для расшифровки
def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                decrypted_char = chr((ord(letter) - ord('А') - shift) % 32 + ord('А'))
            else:
                decrypted_char = chr((ord(letter) - ord('а') - shift) % 32 + ord('а'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += letter
    return decrypted_text

# Получаем данные от пользователя
alphabet_of_exceptions = ' !@#$%^&*()_+{["|\/}]№;%:*-=~1234567890'
while True:
        flag_1 = True
        flag_2 = True
        text = input('Введите текст: ')
        for letter in text:
            if letter == 'ё' or letter == 'Ё':
                flag_1 = False
            if letter not in alphabet_of_exceptions:
                if ord(letter) < 1040 or ord(letter) > 1103:
                    flag_2 = False
        if flag_1 == False:
            print('\n! Ошибка ! Введите текст без буквы "ё"\n')
        elif flag_2 == False:
            print('\n! Ошибка ! Введите текст на русском языке\n')
        else:
            break

while True:
    try:
        shift = int(input('Введите шаг сдвига (целое число): '))
        break
    except ValueError:
        print('\n! Ошибка ! Шаг сдвига должен быть целым числом\n')

# Шифрование
encrypted_text = encrypt(text, shift)
print('Зашифрованный текст:', encrypted_text)

# Расшифровка
decrypted_text = decrypt(encrypted_text, shift)
print('Расшифрованный текст:', decrypted_text)