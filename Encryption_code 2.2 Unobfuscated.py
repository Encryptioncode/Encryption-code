#Encryption code 2.2
import time, socket, shelve, subprocess, string, random, smtplib, ssl
from random import randint
from datetime import date
from datetime import datetime
errnum = 000
def encryption_algorithm1(word):
    letter_number, encrypted_word = 0, ""
    while letter_number < El4Re8W005(word):
        letter = word[letter_number]
        eletter = letter
        eletter = ('q' if letter == 'a' else ('w' if letter == 'b' else ('e' if letter == 'c' else ('r' if letter == 'd' else ('t' if letter == 'e' else ('y' if letter == 'f' else ('u' if letter == 'g' else ('i' if letter == 'h' else ('o' if letter == 'i' else ('p' if letter == 'j' else ('a' if letter == 'k' else ('s' if letter == 'l' else ('d' if letter == 'm' else ('f' if letter == 'n' else ('g' if letter == 'o' else ('h' if letter == 'p' else ('j' if letter == 'q' else ('k' if letter == 'r' else ('l' if letter == 's' else ('z' if letter == 't' else ('x' if letter == 'u' else ('c' if letter == 'v' else ('v' if letter == 'w' else ('b' if letter == 'x' else ('n' if letter == 'y' else ('m' if letter == 'z' else ('*' if (letter == ' ' ) else (' ' if letter == '_' else (',' if letter == '1' else ('.' if letter == '2' else ('/' if letter == '3' else ('<' if letter == '4' else ('>' if letter == '5' else ('?' if letter == '6' else ('`' if letter == '7' else ('~' if letter == '8' else ('1' if letter == '9' else ('2' if letter == '0' else ('3' if letter == '.' else ('4' if letter == '?' else ('5' if letter == '!' else ('6' if letter == ',' else ('7' if letter == ':' else ('8' if letter == '\'' else ('9' if letter == '(' else ('0' if letter == ')' else ('!' if letter == '#' else ('@' if letter == '&' else ('#' if letter == '*' else ('%' if letter == '~' else ('^' if letter == '<' else ('&' if letter == '>' else ('(' if letter == '=' else (')' if letter == '{' else ('ड' if letter == ']' else ('˙' if letter == 'ए' else ('फ' if letter == '-' else ('.' if letter == 'स' else ('*' if letter == 'ग' else ('^' if letter == 'म' else ('%' if letter == 'ल' else ('@' if letter == 'क' else ('!' if letter == 'द' else ('√' if letter == '@' else ('ç' if letter == 'प' else ('˚' if letter == 'ह' else ('µ' if letter == 'फ' else eletter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        encrypted_word, letter_number = encrypted_word + eletter, letter_number + 1 
    clearscreen()
    return encrypted_word
def decryption_algorithm1(encrypted_word):
    letter_number, word = 0, ''
    while letter_number < El4Re8W005(encrypted_word) :
        eletter = encrypted_word[letter_number]
        letter = eletter
        letter = ('a' if eletter == 'q' else ('b' if eletter == 'w' else ('c' if eletter == 'e' else ('d' if eletter == 'r' else ('e' if eletter == 't' else ('f' if eletter == 'y' else ('g' if eletter == 'u' else ('h' if eletter == 'i' else ('i' if eletter == 'o' else ('j' if eletter == 'p' else ('k' if eletter == 'a' else ('l' if eletter == 's' else ('m' if eletter == 'd' else ('n' if eletter == 'f' else ('o' if eletter == 'g' else ('p' if eletter == 'h' else ('q' if eletter == 'j' else ('r' if eletter == 'k' else ('s' if eletter == 'l' else ('t' if eletter == 'z' else ('u' if eletter == 'x' else ('v' if eletter == 'c' else ('w' if eletter == 'v' else ('x' if eletter == 'b' else ('y' if eletter == 'n' else ('z' if eletter == 'm' else (' ' if (eletter == '*' ) else (' ' if eletter == ' ' else ('1' if eletter == ',' else ('2' if eletter == '.' else ('3' if eletter == '/' else ('4' if eletter == '<' else ('5' if eletter == '>' else ('6' if eletter == '?' else ('7' if eletter == '`' else ('8' if eletter == '~' else ('9' if eletter == '1' else ('0' if eletter == '2' else ('.' if eletter == '3' else ('?' if eletter == '4' else ('!' if eletter == '5' else (',' if eletter == '6' else (':' if eletter == '7' else ('\'' if eletter == '8' else ('(' if eletter == '9' else (')' if eletter == '0' else ('#' if eletter == '!' else ('&' if eletter == '@' else ('*' if eletter == '#' else ('~' if eletter == '%' else ('<' if eletter == '^' else ('>' if eletter == '&' else ('=' if eletter == '(' else ('{' if eletter == ')' else (']' if eletter == 'ड' else ('ए' if eletter == '˙' else ('_' if eletter == 'फ' else ('स' if eletter == '.' else ('ग' if eletter == '*' else ('म' if eletter == '^' else ('ल' if eletter == '%' else ('क' if eletter == '@' else ('द' if eletter == '!' else ('@' if eletter == '√' else ('प' if eletter == 'ç' else ('ह' if eletter == '˚' else ('फ' if eletter == 'µ' else letter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        word = word + letter
        letter_number += 1
    clearscreen()
    return word
def encryption_algorithm2(word):
    letter_number, encrypted_word = 0, ""
    while letter_number < El4Re8W005(word):
        letter = word[letter_number]
        eletter = letter
        eletter = ('1' if letter == 'a' else ('2' if letter == 'b' else ('3' if letter == 'c' else ('4' if letter == 'd' else ('5' if letter == 'e' else ('6' if letter == 'f' else ('7' if letter == 'g' else ('8' if letter == 'h' else ('9' if letter == 'i' else ('0' if letter == 'j' else ('q' if letter == 'k' else ('w' if letter == 'l' else ('e' if letter == 'm' else ('r' if letter == 'n' else ('t' if letter == 'o' else ('y' if letter == 'p' else ('u' if letter == 'q' else ('i' if letter == 'r' else ('o' if letter == 's' else ('p' if letter == 't' else ('a' if letter == 'u' else ('s' if letter == 'v' else ('d' if letter == 'w' else ('f' if letter == 'x' else ('g' if letter == 'y' else ('h' if letter == 'z' else ('$' if (letter == ' ') else (' ' if letter == '_' else ('k' if letter == '1' else ('l' if letter == '2' else ('z' if letter == '3' else ('x' if letter == '4' else ('c' if letter == '5' else ('v' if letter == '6' else ('b' if letter == '7' else ('n' if letter == '8' else ('m' if letter == '9' else ('~' if letter == '0' else ('`' if letter == '.' else ('!' if letter == '?' else ('@' if letter == '!' else ('#' if letter == ',' else ('$' if letter == ':' else ('%' if letter == '\'' else ('^' if letter == '(' else ('&' if letter == ')' else ('*' if letter == '#' else ('(' if letter == '&' else (')' if letter == '*' else ('-' if letter == '~' else ('य' if letter == '<' else ('घ' if letter == '>' else ('ब' if letter == '=' else ('छ' if letter == '{' else ('ड' if letter == ']' else ('˙' if letter == 'ए' else ('फ' if letter == '-' else ('.' if letter == 'स' else ('*' if letter == 'ग' else ('^' if letter == 'म' else ('%' if letter == 'ल' else ('@' if letter == 'क' else ('!' if letter == 'द' else ('√' if letter == '@' else ('ç' if letter == 'प' else ('˚' if letter == 'ह' else ('µ' if letter == 'फ' else eletter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        encrypted_word, letter_number = encrypted_word + eletter, letter_number + 1 
    clearscreen()
    return encrypted_word
def decryption_algorithm2(encrypted_word):
    letter_number, word = 0, ''
    while letter_number < El4Re8W005(encrypted_word) :
        eletter = encrypted_word[letter_number]
        letter = eletter
        letter = ('a' if eletter == '1' else ('b' if eletter == '2' else ('c' if eletter == '3' else ('d' if eletter == '4' else ('e' if eletter == '5' else ('f' if eletter == '6' else ('g' if eletter == '7' else ('h' if eletter == '8' else ('i' if eletter == '9' else ('j' if eletter == '0' else ('k' if eletter == 'q' else ('l' if eletter == 'w' else ('m' if eletter == 'e' else ('n' if eletter == 'r' else ('o' if eletter == 't' else ('p' if eletter == 'y' else ('q' if eletter == 'u' else ('r' if eletter == 'i' else ('s' if eletter == 'o' else ('t' if eletter == 'p' else ('u' if eletter == 'a' else ('v' if eletter == 's' else ('w' if eletter == 'd' else ('x' if eletter == 'f' else ('y' if eletter == 'g' else ('z' if eletter == 'h' else (' ' if (eletter == '$' ) else (' ' if eletter == ' ' else ('1' if eletter == 'k' else ('2' if eletter == 'l' else ('3' if eletter == 'z' else ('4' if eletter == 'x' else ('5' if eletter == 'c' else ('6' if eletter == 'v' else ('7' if eletter == 'b' else ('8' if eletter == 'n' else ('9' if eletter == 'm' else ('0' if eletter == '~' else ('.' if eletter == '`' else ('?' if eletter == '!' else ('!' if eletter == '@' else (',' if eletter == '#' else (':' if eletter == '$' else ('\'' if eletter == '%' else ('(' if eletter == '^' else (')' if eletter == '&' else ('#' if eletter == '*' else ('&' if eletter == '(' else ('*' if eletter == ')' else ('~' if eletter == '-' else ('<' if eletter == 'य' else ('>' if eletter == 'घ' else ('=' if eletter == 'ब' else ('{' if eletter == 'छ' else (']' if eletter == 'ड' else ('ए' if eletter == '˙' else ('_' if eletter == 'फ' else ('स' if eletter == '.' else ('ग' if eletter == '*' else ('म' if eletter == '^' else ('ल' if eletter == '%' else ('क' if eletter == '@' else ('द' if eletter == '!' else ('@' if eletter == '√' else ('प' if eletter == 'ç' else ('ह' if eletter == '˚' else ('फ' if eletter == 'µ' else letter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        word = word + letter
        letter_number += 1
    clearscreen()
    return word
def encryption_algorithm3(word):
    letter_number, encrypted_word = 0, ""
    while letter_number < El4Re8W005(word):
        letter = word[letter_number]
        eletter = letter
        eletter = ('œ' if letter == 'a' else ('∑' if letter == 'b' else ('´' if letter == 'c' else ('®' if letter == 'd' else ('†' if letter == 'e' else ('¥' if letter == 'f' else ('¨' if letter == 'g' else ('ˆ' if letter == 'h' else ('ø' if letter == 'i' else ('π' if letter == 'j' else ('å' if letter == 'k' else ('ß' if letter == 'l' else ('∂' if letter == 'm' else ('ƒ' if letter == 'n' else ('©' if letter == 'o' else ('˙' if letter == 'p' else ('∆' if letter == 'q' else ('˚' if letter == 'r' else ('¬' if letter == 's' else ('Ω' if letter == 't' else ('≈' if letter == 'u' else ('ç' if letter == 'v' else ('√' if letter == 'w' else ('∫' if letter == 'x' else ('˜' if letter == 'y' else ('µ' if letter == 'z' else ('0' if (letter == ' ') else (' ' if letter == '_' else ('¡' if letter == '1' else ('™' if letter == '2' else ('£' if letter == '3' else ('¢' if letter == '4' else ('§' if letter == '5' else ('¶' if letter == '6' else ('•' if letter == '7' else ('ª' if letter == '8' else ('º' if letter == '9' else ('1' if letter == '0' else ('2' if letter == '.' else ('3' if letter == '?' else ('4' if letter == '!' else ('5' if letter == ',' else ('6' if letter == ':' else ('7' if letter == '\'' else ('8' if letter == '(' else ('9' if letter == ')' else ('0' if letter == '#' else ('≠' if letter == '&' else (')' if letter == '*' else ('-' if letter == '~' else ('य' if letter == '<' else ('घ' if letter == '>' else ('ब' if letter == '=' else ('छ' if letter == '{' else ('ड' if letter == ']' else ('˙' if letter == 'ए' else ('फ' if letter == '-' else ('.' if letter == 'स' else ('*' if letter == 'ग' else ('^' if letter == 'म' else ('%' if letter == 'ल' else ('@' if letter == 'क' else ('!' if letter == 'द' else ('√' if letter == '@' else ('ç' if letter == 'प' else ('˚' if letter == 'ह' else ('µ' if letter == 'फ' else eletter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        encrypted_word, letter_number = encrypted_word + eletter, letter_number + 1 
    clearscreen()
    return encrypted_word
def decryption_algorithm3(encrypted_word):
    letter_number, word = 0, ''
    while letter_number < El4Re8W005(encrypted_word) :
        eletter = encrypted_word[letter_number]
        letter = eletter
        letter = ('a' if eletter == 'œ' else ('b' if eletter == '∑' else ('c' if eletter == '´' else ('d' if eletter == '®' else ('e' if eletter == '†' else ('f' if eletter == '¥' else ('g' if eletter == '¨' else ('h' if eletter == 'ˆ' else ('i' if eletter == 'ø' else ('j' if eletter == 'π' else ('k' if eletter == 'å' else ('l' if eletter == 'ß' else ('m' if eletter == '∂' else ('n' if eletter == 'ƒ' else ('o' if eletter == '©' else ('p' if eletter == '˙' else ('q' if eletter == '∆' else ('r' if eletter == '˚' else ('s' if eletter == '¬' else ('t' if eletter == 'Ω' else ('u' if eletter == '≈' else ('v' if eletter == 'ç' else ('w' if eletter == '√' else ('x' if eletter == '∫' else ('y' if eletter == '˜' else ('z' if eletter == 'µ' else (' ' if (eletter == '0' ) else (' ' if eletter == ' ' else ('1' if eletter == '¡' else ('2' if eletter == '™' else ('3' if eletter == '£' else ('4' if eletter == '¢' else ('5' if eletter == '§' else ('6' if eletter == '¶' else ('7' if eletter == '•' else ('8' if eletter == 'ª' else ('9' if eletter == 'º' else ('0' if eletter == '1' else ('.' if eletter == '2' else ('?' if eletter == '3' else ('!' if eletter == '4' else (',' if eletter == '5' else (':' if eletter == '6' else ('\'' if eletter == '7' else ('(' if eletter == '8' else (')' if eletter == '9' else ('#' if eletter == '0' else ('&' if eletter == '≠' else ('*' if eletter == ')' else ('~' if eletter == '-' else ('<' if eletter == 'य' else ('>' if eletter == 'घ' else ('=' if eletter == 'ब' else ('{' if eletter == 'छ' else (']' if eletter == 'ड' else ('ए' if eletter == '˙' else ('_' if eletter == 'फ' else ('स' if eletter == '.' else ('ग' if eletter == '*' else ('म' if eletter == '^' else ('ल' if eletter == '%' else ('क' if eletter == '@' else ('द' if eletter == '!' else ('@' if eletter == '√' else ('प' if eletter == 'ç' else ('ह' if eletter == '˚' else ('फ' if eletter == 'µ' else letter)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        word = word + letter
        letter_number += 1
    clearscreen()
    return word
def G189HF00(G189HF01):
    print(G189HF01[::-1])
def printfromend(phrase, toprintlater):
    length = len(phrase)
    repeater = -1
    try:
        while True:
            print(phrase[repeater:length])
            print(toprintlater)
            printthelast()
            repeater -= 1
            time.sleep(0.01)
            clearscreen()
            if repeater * -1 > length:
                print(phrase[repeater:length])
                break
    except:
        print('')
def clearscreen(): 
    print('\n' * 50)
def El4Re8W005(text):
    text = text + '∞'
    letter_number = 0
    letter = ' '
    while letter != '∞':
        letter = text[letter_number]
        letter_number += 1
    letter_number = letter_number - 1
    return letter_number
def checkinternet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return 'connected to internet'
    except socket.error as ex:
        error = (ex)
        return 'internet connection offline'
def printthelast():
     print('\n\n\n\n\n\n\n\n  __________    __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /          \  /          \ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/   Account  \/  Settings  \ '), time.sleep(0.07)
def smooth_mainmenu():
    from datetime import date
    now = datetime.now()
    timenow = now.strftime("%H:%M:%S")
    today = date.today()
    date = today.strftime("%B %d, %Y")
    print('   _________'), time.sleep(0.07), clearscreen() ,print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(), print('   __________'),print('  /          \    _________'),print(' /   Encrypt  \  /         \  _________'), time.sleep(0.07), clearscreen(),print('  __________    __________'),print(' /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \ /  Privacy \  _________ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________'),print(' /          \  /          \  /  Privacy \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \ /          \   _________ '), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /          \   __________ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/   Account  \ /          \ '), time.sleep(0.07), clearscreen(), printthelast()
    intcon = checkinternet()
    clearscreen()
    print('   ',date,'    ',timenow,'    ',intcon,'    ',signinornot)
    printthelast()
def alg_choose_decrypting(todec,alg):
    if alg == '1':
        todec1 = decryption_algorithm1(todec)
    elif alg == '2':
        todec1 = decryption_algorithm2(todec)
    else:
        todec1 = decryption_algorithm3(todec)
    encryption_animation(todec,todec1)
    clearscreen()
    input('The Decrypted text is the following: '+todec1)
def encryption_animation(phrase, encrypted_phrase):
    global animation_speed
    phraselength = len(phrase)
    wait_time, cut1, halfcut, cut2 , counter = (0.09 if phraselength <= 10 else (0.07 if phraselength <= 20 else (0.05 if phraselength <= 35 else (0.04 if phraselength <= 50 else (0.03 if phraselength <= 75 else (0.02)))))), 0, int(round(phraselength/2,0)), 0, 0
    while counter <= 7:
        print(phrase,'\nYour Encrypted text is being generated','.'*counter), time.sleep(0.07), clearscreen()
        counter += 1
    counter = 0
    while (cut2 + halfcut) < phraselength:
        cut2interpreter = cut2 + halfcut
        toprint = (encrypted_phrase[:cut1] if cut1 <= halfcut else encrypted_phrase[:halfcut])  + phrase[cut1:halfcut] + encrypted_phrase[halfcut:cut2interpreter] + phrase[cut2interpreter:phraselength]
        toprint = toprint
        print(toprint), print('Your Encrypted text is being generated','.'* round(counter)), time.sleep(wait_time), clearscreen()
        counter, cut1, cut2 = 1 if counter >= 7 else counter + 0.33, cut1 + 1 if phraselength <= 768 else (cut1 if cut1 == halfcutcut else (cut1 + 6)), cut2 + 1 if phraselength <= 768 else cut2 + 6
    counter = 0
    while counter <= 7:
        clearscreen(),print(encrypted_phrase,'\nYour Encrypted text is being generated','.'*counter), time.sleep(0.07)
        counter += 1
def server_send_email(receiver_email,message):
    smtp_car = (decryption_algorithm3('∂©´2ßøœ∂¨2˙Ω∂¬'[::-1]))
    port = int(decryption_algorithm1('`~>'[::-1]))
    sender_email = decryption_algorithm2('et3`w91e7√54t3rt9pygi3r5`i5si5o'[::-1])
    password = (decryption_algorithm1(decryption_algorithm1('fyybv^yugmifatyz'[::-1])))
    context = ssl.create_default_context()
    try:
        car = smtplib.SMTP(smtp_car,port)
        car.ehlo()
        car.starttls(context=context) # Secure the connection
        car.ehlo()
        car.login(sender_email, password)
        car.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        car.quit()
def shelvewrite(textfilename,towrite):
    textfilenametxt = textfilename + '.txt'
    writer = shelve.open(str(textfilenametxt))
    writer[str(textfilename)] = towrite
    writer.close()
def shelveread(textfilename):
    textfilenametxt = textfilename + '.txt'
    reader = shelve.open(str(textfilenametxt))
    text = reader[str(textfilename)]
    reader.close()
    return text
def shelveappend(textfilename, toappend): #append to text file
    textfilenametxt = textfilename + '.txt'
    read = shelveread(textfilename)
    toappend = (read, toappend)
    shelvewrite(textfilename, toappend)
try:
    high = shelveread('EncryptionCode2.2')
except:
    shelvewrite('EncryptionCode2.2','hi')
    print('Welcome to Encryption code 2.2 Please create you account or continue as a guest')
choice = 'start'
animvar,pwdask, = 'on','ask'
try:
    signinornot = shelveread('signin')
except:
    shelvewrite('signin','signed out')
    signinornot = 'signed out'
while choice != 'q':
    #try:
        errnum = 400
        smooth_mainmenu()
        today = date.today()
        if today.strftime("%B") == 'March' or today.strftime("%B") == 'April' or today.strftime("%B") == 'May':
            placeholder = ''
        else:
            print("A new version of Encryption code is available! Be sure to update!")
        print('Type the first letter of your choice followed by enter: ', end = '')
        choice = input('')
        errnum = 401
        clearscreen(), print('  __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /  About   \   __________ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/  This code \ /          \ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \ /   About  \   _________ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \ /          \   _________'), time.sleep(0.07), clearscreen(), print('  __________    __________    __________'),print(' /          \  /          \  /  Privacy \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________'),print(' /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \ /  Privacy \  _________ '), time.sleep(0.07), clearscreen(),  print('   __________'),print('  /          \    _________'),print(' /   Encrypt  \  /         \  _________'), time.sleep(0.07), clearscreen(),print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(),print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(),print('   _________'), time.sleep(0.07), clearscreen() 
        if 'e' == choice :
            word, yeno = ' ', 'n'
            if True:
                clearscreen()
                word = input(43 * ' '+'Type in a message to encrypt:   \n'+ 43 * ' ')
                errnum = 402
                randomgenpass = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(randint(999,10000))
                randomgenpass1 = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(randint(999,10000))
                randompass = randomgenpass+'-'+randomgenpass1
                mover = 70
                while mover >= 35 and (animvar == 'on' and pwdask == 'always ask'):
                    clearscreen()
                    print(43 * ' ','Type in a message to encrypt:   \n',43 * ' ', word, '\n')
                    print((70 - mover)*' ', 'Type an encryption Password if you want to set one'), print(mover*' ', 'If you would not like to set a password, press enter.'), print((70 - mover)*' ', 'To use a randomly generated hard to guess password: "',randompass,'" press r and enter')
                    time.sleep(0.035)
                    mover = (mover - 5 if mover > 60 else (mover - 4 if mover > 55 else (mover - 3 if mover > 45 else (mover - 2 if mover > 35 else mover - 1))))
                mover = 35
                errnum = 403
                clearscreen(), print(43 * ' ','Type in a message to encrypt:   \n',43 * ' ', word, '\n')
                if pwdask == 'ask':
                    print((70 - mover)*' ', 'Type an encryption Password if you want to set one'), print(mover*' ', 'If you would not like to set a password, press enter.'), print((70 - mover)*' ', 'To use a randomly generated hard to guess password: "',randompass,'" press r and enter')
                    fish = input((43 * ' ')+'')
                else:
                    fish = ''
                if fish.upper() == 'R':
                    pwd = randompass
                elif fish == '':
                    pwd = 'no pwd'
                else:
                    pwd = fish
            errnum = 404
            if 'क' in word or 'द' in word or 'व' in word or 'ए' in word or 'र' in word or 'त' in word or 'क' in word or 'य' in word or 'उ' in word or 'ऊ' in word or 'इ' in word or 'ई' in word or 'ओ' in word or 'प' in word or 'आ' in word or 'स' in word or 'ड' in word or 'फ' in word or 'ग' in word or 'ह' in word or 'ज' in word or 'ल' in word or 'ज' in word or 'च' in word or 'व' in word or 'ब' in word or 'न' in word or 'ण' in word or 'म' in word:
                input(' Marathi/Hindi language detected. Press enter to automatically optimize settings for encryption')
            if 'è' in word or 'é' in word or 'ú' in word or 'í' in word or 'ì' in word or 'ó' in word or 'ò' in word or 'à' in word or 'á' in word or 'ś' in word or 'ć' in word or 'ć' in word or 'ñ' in word or 'ń' in word or ' de ' in word:
                input(' Spanish language detected. Press enter to automatically optimize settings for encryption')
            try:
                previously_encrypted = shelveread('2.0')
            except:
                previously_encrypted = ' '
            errnum = 405
            previously_encrypted = previously_encrypted + '\n\n' + word 
            shelvewrite('2.0',previously_encrypted )     
            if True:
                algorithm = randint(1,3)
                if algorithm == 1:
                    word1 = '6' + encryption_algorithm1(word) + 'Œ' + (encryption_algorithm1(encryption_algorithm1(pwd)))[::-1] 
                elif algorithm == 2:
                    word1 = '7' + encryption_algorithm2(word) + '´' + (encryption_algorithm1(encryption_algorithm1(pwd)))[::-1]
                else :
                    word1 = '8' + encryption_algorithm3(word) + '˛' + (encryption_algorithm1(encryption_algorithm1(pwd)))[::-1]
            mover = 50
            word = 'Text: '+ word + '  password: ' + pwd
            word2 = 'Encrypted text:' + word1
            encryption_animation(word,word2)
            clearscreen(), print(word2)
            errnum = 406
            if input() != 's':
                subprocess.run("pbcopy", universal_newlines=True, input=word1)
        if 'd' == choice :
            try:
                mover = 100
                while mover >= 50 and animvar == 'on':
                    clearscreen()
                    print(mover * ' ','Decryption'), print((100 - mover)*' '+ 'Paste a message to decrypt below')
                    time.sleep(0.035)
                    mover = (mover - 5 if mover > 90 else (mover - 4 if mover > 80 else (mover - 3 if mover > 70 else (mover - 2 if mover > 60 else mover - 1)))) 
                mover = 50
                clearscreen()
                print(mover * ' ','Decryption'), print((100 - mover)*' '+ 'Paste a message to decrypt below')
                errnum = 407
                todec = input()
                num = 0
                alg = todec[num]
                while alg == ' ':
                    alg = todec[num]
                    num += 1
                todec = todec.replace(alg,'')
                alg = str(int(alg) - 5)
                passnum = 0
                extractpwd = ''
                scanner = 'start'
                while scanner != '˛' and scanner != '´' and scanner != 'Œ':
                    scanner = todec[passnum]
                    passnum += 1
                try:
                    while True:
                        extractpwd = extractpwd + todec[passnum]
                        passnum += 1
                except:
                    knownpwd = (decryption_algorithm1(decryption_algorithm1(extractpwd)))
                errnum = 408
                try:
                    read = shelveread('locker')
                except:
                    shelverwrite('locker','')
                todec = todec.replace(extractpwd,'')
                if '˛' in todec:
                    todec = todec.replace('˛','')
                if '´' in todec:
                    todec = todec.replace('´','')
                if 'Œ' in todec:
                    todec = todec.replace('Œ','')
                knownpwd = knownpwd[::-1]
                if knownpwd != 'no pwd' :
                    if (todec not in read) and (knownpwd not in read):
                        trypwd = input('This encrypted message is password protected. Please enter password to decrypt ')
                        if trypwd == knownpwd:
                            alg_choose_decrypting(todec, alg)
                        else:
                            trypwd = input('Wrong password. Try again. After 2 more tries you will be locked out. ')
                            if trypwd == knownpwd:
                                alg_choose_decrypting(todec, alg)
                            else:
                                trypwd = input('Wrong password. Try again. After 1 more try you will be locked out. ')
                                if trypwd == knownpwd:
                                    alg_choose_decrypting(todec, alg)
                                else:
                                    trypwd = input('Wrong password. Try again. After this try you will be locked out. ')
                                    if trypwd == knownpwd:
                                        alg_choose_decrypting(todec, alg)
                                    else:
                                        read = shelveread('locker')
                                        towrite = read + todec +  '   ' + knownpwd       
                                        shelvewrite('locker',towrite)
                                        print('Wrong password. you have been locked out of this message.')
                                        input('press enter to return to the main menu')
                    else:
                        print('You have been locked out of this message.')
                        print('contact the owner to send you the message with a new password')
                        input('press enter to return to the main menu')
                else:
                     alg_choose_decrypting(todec, alg)
            except:
                input('The message was not recognized. Press enter to return to the main menu')
        if 'p' == choice :
            errnum = 409
            print('The encryption code has updated its privacy policy'), time.sleep(0.3), print('To view the full privacy policy, click the link: https://sites.google.com/view/encryptioncode/privacy-policy'), time.sleep(0.3), print('View the privacy policy summary below'), time.sleep(0.3), print('  -Your Encrypted messages are NOT stored in the encryption code server after being processed'), time.sleep(0.3), print('  -Your passwords WILL be stored in the encryption code server for verification when decryption is attempted'), time.sleep(0.3), print('  -ONLY your Encrypted messages and passwords are sent to the server to be processed. All your other activity on encryption code is not sent to the server'), input('press enter to return to thr main menu')
        if choice == 'c':
            errnum = 410
            print('you can contact customer service at skparab1@gmail.com '), print('\nYou can also fill out the customer service form:'), print('https://forms.gle/227eb5WRo3hRAnmw6'), input()
        if choice == 'm':
            errnum = 411
            try:
                previously_encrypted = shelveread('2.0')
            except:
                shelvewrite('2.0','')
                previously_encrypted = ''
            print('you have no memory stored' if previously_encrypted == ' ' else ''), print(previously_encrypted), print('Welcome to memory\nThe previously encrypted messages are above in their respective order')
            hmm = input('\n would you like to clear memory? press y or enter for no')
            if hmm == 'y':
                shelvewrite('2.0','')
                previously_encrypted = ''
        if choice == 's':
            errnum = 412
            say = 'start'
            while say != 'm':
                mover = 80
                while mover >= 40 and animvar == 'on':
                    clearscreen()
                    print(mover * ' ','Animation             ',animvar), print((80 - mover)*' '+ 'Encryption password    ',pwdask,'\n'), print(mover * ' ','Press a to enable/diable animations'), print((80 - mover)*' '+ 'Press p to change password settings'), print(mover * ' ','Press m save changes and return to the main menu'), print((80 - mover)*' '+ 'press d to return to factory default settings')
                    time.sleep(0.035)
                    mover = (mover - 5 if mover > 70 else (mover - 4 if mover > 65 else (mover - 3 if mover > 60 else (mover - 2 if mover > 50 else mover - 1)))) 
                mover = 40
                clearscreen(), print(mover * ' ','Animation             ',animvar), print((80 - mover)*' '+ 'Encryption password    ',pwdask,'\n'), print(mover * ' ','Press a to enable/diable animations'), print((80 - mover)*' '+ 'Press p to change password settings'), print(mover * ' ','Press m save changes and return to the main menu'), print((80 - mover)*' '+ 'press d to return to factory default settings')
                say = input()
                animvar = ('on' if animvar == 'off' else 'off') if say == 'a' else animvar
                pwdask = ('ask' if pwdask == 'never use password' else 'never use password') if say == 'p' else pwdask
                pwdask = 'ask' if say == 'd' else pwdask
                animvar = 'on' if say == 'd' else animvar
        if choice == 'a' and signinornot != 'signed out' :
            errnum = 413
            print(signinornot)
            print('Welcome to your Encryption code account dashboard')
            print('Press s to sign out of your Encryption code account')
            print('Press e to edit your account details or change password')
            print('Press l to see your Encryption code login records')
            print('Press a to change your account settings')
            print('Press t for Encryption code server to send a test email')
            ans = input('Type your choice followed by enter: ')
            if ans == 's':
                signinornot = 'signed out'
                shelvewrite('signin',signinornot)
                print('You are now signed out of your Encryption code account')
                input('press enter to continue to the main menu')
                now,today = datetime.now(), date.today()
                time,date = now.strftime("%H:%M:%S"), today.strftime("%B %d, %Y")
                whattowrite = ('signed out    ',time,'    ',date)
                shelvewrite('user1log',whattowrite)
            if ans == 'e':
                text = shelveread('user1')
                text.split
                print(' Here\'s what we have from you')
                print('Username: ' + text[1])
                print('First name: ' + text[3])
                print('Last name: ' + text[5])
                print('Email: ' + text[4])
                print('Welcome to your Encryption code account dashboard')
                print('Press f to change your registered first name')
                print('Press l to change your registered last name')
                print('Press e to change your registered email')
                print('Press p to change your password')
                ans = input('Type your choice followed by enter: ')
                newfname,newlname,newemail,newpass = text[3], text[5], text[4], text[2]
                if ans == 'f':
                    newfname = input('Enter your new first name')
                if ans == 'l':
                    newlname = input('Enter your new last name')
                if ans == 'e':
                    newemail = input('Enter your new email address')
                if ans == 'p':
                    print('To keep you account safe, Encryption code must verify that it is actually you.')
                    print('Encryption code server is sending an email to your registered email address. Please wait.'), time.sleep(0.07),print('Encryption code server is sending an email to your registered email address. Please wait..'), print('Encryption code server is sending an email to your registered email address. Please wait...'), time.sleep(0.07),print('Encryption code server is sending an email to your registered email address. Please wait....')
                    try:
                        pinsend = randint(111111,999999)
                        msg = """\
                        Subject: <server.encryptioncode>  Change password request

                        You requested to change password.
                        Here is your one time pin:  """, pinsend,"""
                        Do not share this with anyone! We will never contact you for it."""
                        #server_send_email(text[4],msg)
                    except:
                        print('Were sorry, but the Encryption code server was not able to process your request.'), print('It is likely that the server is temporarily down. please try again later.')   
                    finally:
                        print('an email with a one time verification pin has been sent to your email address')
                    yay = input('enter pin here: ')
                    if pinsend == str(yay):
                        newpass = input('Enter your new password')
                    else:
                        print('Wrong pin. Try again')
                writer = shelve.open('user1.txt')
                writer['user1'] = [text[1], newpass, newfname, newemail, newlname]
                writer.close()
            if ans == 'l':
                read = shelveread('user1log')
                print(read)
                input('View your log above. press enter to continue')
            if ans == 'a':
                blank = ''
                #change account settings
        if choice == 'a' and signinornot == 'signed out':
            print('Hello')
            print('Press s to sign into your Encryption code account')
            print('Press c to create a new Encryption code account')
            ans = input('Type your choice followed by enter: ')
            if ans == 's':
                clearscreen()
                while signinornot == 'signed out':
                    print(' Encryption code         Sign in\n Forgot password? type your username and type "forgot" in password space\n')
                    usnm = input(' Username: ',end = '')
                    pswd = input('\n Password: ',end = '')
                    text = shelveread('user1')
                    text.split
                    if pswd == 'forgot':
                        while i in range (1,5):
                            print('Encryption code server is sending an email to your registered email address. Please wait.'), time.sleep(0.07),print('Encryption code server is sending an email to your registered email address. Please wait..'), print('Encryption code server is sending an email to your registered email address. Please wait...'), time.sleep(0.07),print('Encryption code server is sending an email to your registered email address. Please wait....')
                        try:
                            pinsend = randint(111111,999999)
                            msg = """\
                            Subject: <server.encryptioncode>  Change password request

                            You requested to change password.
                            Here is your one time pin:  """, pinsend,"""
                            Do not share this with anyone! We will never contact you for it."""
                            #server_send_email(text[4],msg)
                        except:
                            print('Were sorry, but the Encryption code server was not able to process your request.'), print('It is likely that the server is temporarily down. please try again later.')
                        pin = input('Encryption code server has sent a password reset pin to your email address. check your email and type it here: ')
                        #verify pin
                    # data stored as follows: 1.username  2.password 3.first name 4. email 5. last name
                    if text[1] == usnm and text[2] == pswd:
                        signinornot = 'Hi, ' + text[3]
                        shelvewrite('signin', signinorout)
                        print('Hi, ' + text[3])
                        print('You are now signed in to your Encryption code account')
                        input('press enter to continue to the main menu')
                        now,today = datetime.now(),date.today()
                        time,date = now.strftime("%H:%M:%S"), today.strftime("%B %d, %Y")
                        whattowrite = ('signed in    ',time,'    ',date)
                        shelveappend('user1log',whattowrite)
                        break
                    else:
                        clearscreen()
                        print('Username or password is incorrect. Try again')
            if ans == 'c':
                clearscreen()
                print(' Encryption code        Create account\n\n')
                fname = input('Type your first name: ')
                lname = input('\nType your last name: ',)
                usnm = input('\nCreate an account Username: ',)
                pswd = input('\nCreate an account Password. Must be at lease 8 letters long and have at least one number: ')
                email = input('\nType your email. Note: email will only be used to send reset password pin and 2 step veification, if enabled: ')
                writer = shelve.open('user1.txt')
                writer['user1'] = [usnm, pswd, fname, email, lname]
                writer.close()
                now,today = datetime.now(),date.today()
                time,date = now.strftime("%H:%M:%S"), today.strftime("%B %d, %Y")
                whattowrite = ('signed in    ',time,'    ',date)
                shelvewrite('user1log',whattowrite)
            #about encryption code > put somewhere later
            mover = 100
            #clearscreen(), print(mover * ' ','About Encryption code'), print((101 - mover)*' '+ 'Version            2.1'), print(mover * ' ','Release date       Sunday, April 24'), print((101 - mover)*' '+ 'Author:            Encryption code software team'), print(mover * ' ','File size          36 KB'), print((101 - mover)*' '+ 'Connection:        ' + connection), print(mover * ' '+' Press enter to return to the main menu')
            input()
            errnum = 414
        errnum = 415
    #except Exception as e:
        #print(e), input('Hmm... An error number '+ str(errnum) + ' occurred. Sorry about that. press enter to try again. If this continues, contact our customer service team with error code '+ str(errnum) + '. This will help our software team locate and fix the error')
