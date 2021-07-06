import vk_api
import json
import time


def logs():
    with open("logs.json", 'r') as pass_file:
        log_data = json.loads(pass_file.read())
        user_login = log_data['login']
        user_password = log_data['password']
        return user_login, user_password


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def auth():
    login, password = logs()
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    vk = vk_session.get_api()
    try:
        vk_session.auth()
        return vk
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return


def status_change(vk):
    stat = vk.account.getProfileInfo()
    stat = stat['status']   # aka 'v_17.366'
    version = stat[2:]
    v_year = version[:2]
    v_day = version[3:]
    # Проверка, високосный ли год >
    current_year = time.strftime('%Y')
    if (int(current_year) % 4 == 0) and (int(current_year) % 100 != 0) or (int(current_year) % 400 == 0):
        amount = '366'
    else:
        amount = '365'
    if v_day == amount:
        v_day = "000"
        v_year = str(int(v_year) + 1)
        # version = float(version[:2] + "." + part) + 1
        # version = str(version)
    else:
        v_day = str(int(v_day) + 1)
        while len(v_day) != 3:
            v_day = "0" + v_day
        # version = float(version) + 0.001
        # version = str(version)[:6]
        # print(version)
    stat = "v_" + v_year + "." + v_day
    vk.account.saveProfileInfo(status=stat)
    time.sleep(86400)
    # status_change(vk)


if __name__ == '__main__':
    vk = auth()
    time_now = time.strftime('%X')
    while time_now != "21:00:00":
        time.sleep(1)
        time_now = time.strftime('%X')
        print("Wrong time = " + time_now)
    print("Time: " + time_now)
    while True:
        status_change(vk)
