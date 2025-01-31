##########IMPORT##########
import os
import time
import sys
import json
import random

try:
    import requests
    from prettytable import PrettyTable
except:
    os.system('pip install requests')
    os.system('pip install prettytable')
    import requests
    from prettytable import PrettyTable
##########IMPORT##########

#---LIST USERAGENT---#
list_useragents = [
    "android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
    "android|Mozilla/5.0 (Linux; Android 13; Pixel 6a Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G928I Build/MMB29K) AppleWebKit/602.37 (KHTML, like Gecko) Chrome/49.0.2276.245 Mobile Safari/535.1"
]
#---LIST USERAGENT---#

###########DEF############
def logo(animation): #---LOGO---#
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
{CSB(2, 0)}{CSB(1, 11)}╔═════════════════════════════════════════════════════════════════════════╗
{CSB(2, 0)}{CSB(1, 11)}║                                      {CSB(1, 166)}【】{CSB(1, 10)}╔════════════════════════════╗ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 46)}●●●●      ●●  ●●●●●         ●●●      {CSB(1, 166)}【】{CSB(1, 46)}║     GOLIKE THREAD TOOL     ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 47)}●● ●●     ●●  ●●   ●●      ●● ●●     {CSB(1, 166)}【】{CSB(1, 47)}║                            ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 48)}●●  ●●    ●●  ●●    ●●    ●●   ●●    {CSB(1, 166)}【】{CSB(1, 48)}║ Create by: NDA MOD         ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 49)}●●   ●●   ●●  ●●     ●●  ●●●●●●●●●   {CSB(1, 166)}【】{CSB(1, 49)}║ Version: {CURRENT_VERSION}             ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 50)}●●    ●●  ●●  ●●    ●●  ●●       ●●  {CSB(1, 166)}【】{CSB(1, 50)}║ Python: 3.12               ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 51)}●●     ●● ●●  ●●   ●●  ●●         ●● {CSB(1, 166)}【】{CSB(1, 51)}║                            ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║ {CSB(1, 123)}●●      ●●●●  ●●●●●   ●●           ●●{CSB(1, 166)}【】{CSB(1, 123)}║                            ║ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}║                                      {CSB(1, 166)}【】{CSB(1, 87)}╚════════════════════════════╝ {CSB(1, 11)}║
{CSB(2, 0)}{CSB(1, 11)}╚═════════════════════════════════════════════════════════════════════════╝{CSB(2, 0)}"""
    os.system('cls' if os.name == 'nt' else 'clear')
    if animation==1:
        lines = logo.splitlines()
        for line in lines:
            for i in range(1, len(line) + 1):
                print(line[:i], flush=True, end="\r")
                time.sleep(0.0025)
            time.sleep(0.004)
            print()
    elif animation==0:
        print(logo)


def status_run_display(idgolike_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager): #---STATUS JOB RUN DISPLAY---#
    table = PrettyTable()
    table.field_names = [f"{CSB(2, 1)}{CSB(1, 123)}ID{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 201)}USER{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 172)}THREAD{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 99)}LIKE{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 129)}FOLLOW{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 11)}MONEY{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 27)}STATUS{CSB(2, 0)}"]
    for i in range(slgolike):
        table.add_row([f"{CSB(2, 1)}{CSB(1, 123)}{idgolike_manager[i]}{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 207)}{username_manager[i]} {CSB(1, 154)}[ {coin_manager[i]} ]{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 83)}{thread_manager[i]+1}/{slthread_manager[i]}{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 99)}{joblike_manager[i]}{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 129)}{jobfollow_manager[i]}{CSB(2, 0)}",
                        f"{CSB(2, 1)}{CSB(1, 11)}{tongxu_manager[i]} VND{CSB(2, 0)}",
                        f"{CSB(2, 1)}{status_manager[i]}{CSB(2, 0)}"])
    table.align = "c"
    print(table)


def CSB(x1, x2): #---CUSTOM COLOR-STYLE---#
    if x1 == 1:
        if x2 > 255:
            x3 = random.randint(1, 255)
            color = f"\033[38;5;{x3}m"
        elif 1 <= x2 <= 255:
            color = f"\033[38;5;{x2}m"
        return color
    elif x1 == 2:
        style = f"\033[{x2}m"
        return style
    elif x1 == 3:
        if x2 > 255:
            x3 = random.randint(1, 255)
            background = f"\033[48;5;{x3}m"
        elif 1 <= x2 <= 255:
            background = f"\033[48;5;{x2}m"
        return background
    return ""


def countdown(time_sec): #---COUNDOWN---#
    while time_sec >= 0:
        print(f"{CSB(2, 1)}{CSB(1, 256)}Please wait: {time_sec}", flush=True, end="\r")
        time.sleep(1)
        print("\033[2K", end="")
        time_sec -= 1
    print("\033[2K", end="")


def check_and_update(current_version, current_versioncode): #---CHECK & UPDATE---#
    logo(1)
    print(f"{CSB(2, 1)}{CSB(1, 11)} Checking Update...")
    try:
        data = requests.get(f"https://raw.githubusercontent.com/ndamod/GolikeToolThread/main/Update.json").json()
        latest_versioncode = int(data["versioncode"])
        latest_version = str(data["version"])
        if int(current_versioncode) < latest_versioncode:
            print(f"{CSB(2, 1)}{CSB(1, 11)}Updating from version {current_version} to {latest_version}...")
            update_data = requests.get(data["update_file"]).content
            with open("Main.py", "wb") as file:
                file.write(update_data)
            print(f"{CSB(2, 1)}{CSB(1, 10)}Update successful! Restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)
        elif int(current_versioncode) > latest_versioncode:
            print(f"{CSB(2, 1)}{CSB(1, 11)}You are running the beta version.")
        else:
            print(f"{CSB(2, 1)}{CSB(1, 123)}You are using the latest version.")
    except Exception as e:
        print(f"{CSB(2, 1)}{CSB(1, 9)}Error while checking or updating: {e}")


def get_user_data(): #---GET INPUT DATA---#
    logo(1)
    AccountData = requests.get("https://raw.githubusercontent.com/ndamod/GolikeToolThread/main/AccountData.json").json()
    slgolike = len(AccountData)
    idgolike_manager = []
    token_manager = []
    username_manager = []
    coin_manager = []
    thread_manager = []
    slthread_manager = []
    joblike_manager = []
    jobfollow_manager = []
    tongxu_manager = []
    status_manager = []
    for idgolike in range(slgolike):
        idgolike_manager.append(idgolike)
        token_manager.append(str(AccountData[idgolike]['token']))
        username_manager.append(str(AccountData[idgolike]['name']))
        headers = {
            'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="125", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent': User_Agent,
            "Authorization" : token_manager[-1],
            'Content-Type':'application/json;charset=utf-8'
        }
        print(f'{CSB(1, 11)}Logging in {str(AccountData[idgolike]['name'])}')
        url1 = 'https://gateway.golike.net/api/users/me'
        checkurl1 = ses.get(url1,headers = headers).json()
        if checkurl1['status'] == 200 :
            coin = checkurl1['data']['coin']
            slthread = len([data['name'] for data in requests.get('https://gateway.golike.net/api/threads-account', headers=headers).json()['data']])
            coin_manager.append(coin)
            slthread_manager.append(slthread)
            ses.headers.update(headers)
            thread_manager.append(0)
            joblike_manager.append(0)
            jobfollow_manager.append(0)
            tongxu_manager.append(0)
            status_manager.append("Stopping")
            print(f'{CSB(2, 1)}{CSB(1, 10)}Login successful👤')
            time.sleep(1.5)
    return slgolike, idgolike_manager, token_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager


def THREADS(): #---DO JOB THREAD---#
    global joblike_manager
    global jobfollow_manager
    global tongxu_manager
    logo(0)
    status_run_display(idgolike_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager)
    user_THREADS = []
    account_id1 = []
    checkaccount = requests.get('https://gateway.golike.net/api/threads-account',headers=headers).json()
    for data in checkaccount['data'] :
            user_THREADS.append(data['name'])
            account_id1.append(data['id'])
    if int(thread_manager[golike]) >=0 or int(thread_manager[golike]) < len(user_THREADS) :
        user_THREADS = user_THREADS[int(thread_manager[golike])]
        account_id = account_id1[int(thread_manager[golike])]
        param = {
             'account_id':str(account_id)
        }
        while True:
            try:
                job = 'https://gateway.golike.net/api/advertising/publishers/threads/jobs?account_id='+str(account_id)
                nos = ses.get(job,headers=headers,params=param).json()
                if nos['status'] ==200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    countdown(int(random.randint(8, 15)))
                    url = 'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs'
                    json_data = {
                    'account_id': account_id,
                    'ads_id': ads_id,
                    }
                    response = requests.post(
                    'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',
                    headers=headers,
                    json=json_data,
                    ).json()
                    if response['success']==True:
                        prices =response['data']['prices']
                        tongxu_manager[golike] += prices
                        if type == 'follow':
                            jobfollow_manager[golike] +=1
                            logo(0)
                            status_run_display(idgolike_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager)
                            print(f'{CSB(2, 1)}{CSB(1, 93)}║ {CSB(1, 129)}{type}{CSB(1, 93)} ║ {CSB(1, 213)}{ads_id}{CSB(1, 93)} ║ {CSB(1, 11)}+{prices} VND{CSB(1, 93)} ║')
                        elif type == 'like':
                            joblike_manager[golike] +=1
                            logo(0)
                            status_run_display(idgolike_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager)
                            print(f'{CSB(2, 1)}{CSB(1, 93)}║ {CSB(1, 99)}{type}{CSB(1, 93)}   ║ {CSB(1, 213)}{ads_id}{CSB(1, 93)} ║ {CSB(1, 11)}+{prices} VND{CSB(1, 93)} ║')
                    else:
                        type_job = type
                        skip_job(ads_id, account_id, object_id, type_job)
                else:
                    print(f'{CSB(1, 196)}{str(nos['message'])}')
                    countdown(3)
                    print("\033[F\033[K", end='')
                    break
            except TypeError :
                type_job = type
                skip_job(ads_id, account_id, object_id, type_job)


def skip_job(ads_id, account_id, object_id, type_job): #---SKIP JOB---#
    skipjob = 'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs'
    PARAMS = {
    'ads_id' : ads_id,
    'account_id' : account_id,
    'object_id' : object_id,
    'async': 'true',
    'data': 'null',
    'type': type_job,
    }
    checkskipjob = ses.post(skipjob,params=PARAMS).json()
    if checkskipjob['status'] == 200:
        PARAMS = {
        'ads_id' : ads_id,
        'account_id' : account_id,
        'object_id' : object_id,
        'async': 'true',
        'data': 'null',
        'type': type_job,
        }


###########DEF############

#######MAIN CODE#########
if __name__ == "__main__":
    CURRENT_VERSIONCODE = "35020250131"
    CURRENT_VERSION = "3.5.0"
    ses = requests.Session()
    User_Agent = random.choice(list_useragents)
    check_and_update(CURRENT_VERSION, CURRENT_VERSIONCODE)
    time.sleep(2)
    slgolike, idgolike_manager, token_manager, username_manager, coin_manager, thread_manager, slthread_manager, joblike_manager, jobfollow_manager, tongxu_manager, status_manager = get_user_data()
    
    logo(1)
    while True:
        for golike in range(slgolike):
            headers = {
                'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
                'Referer':'https://app.golike.net/',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="125", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':"Windows",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
                'User-Agent': User_Agent,
                "Authorization" : token_manager[golike],
                'Content-Type':'application/json;charset=utf-8'
            }
            status_manager[golike] = f"{CSB(2, 1)}{CSB(1, 10)}Running{CSB(2, 0)}"
            for vlxx in range(slgolike):
                if vlxx != golike:
                    status_manager[vlxx] = f"{CSB(2, 1)}{CSB(1, 9)}Stopping{CSB(2, 0)}"
            if int(slthread_manager[golike]) > 1:
                for thread_manager[golike] in range(int(slthread_manager[golike])):
                    while True:
                        try:
                            THREADS()
                            break
                        except Exception as e:
                            print(f"{CSB(1, 256)}Network error. Try it again after 30 seconds. {e}", flush=True, end="\r")
                            time.sleep(30)
                            print("\033[2K", end="")
            else:
                thread_manager[golike] = 0
                while True:
                    try:
                        THREADS()
                        break
                    except Exception as e:
                        print(f"{CSB(1, 256)}Network error. Try it again after 30 seconds. {e}", flush=True, end="\r")
                        time.sleep(30)
                        print("\033[2K", end="")
            countdown(random.randint(600, 1800))
#######MAIN CODE#########
