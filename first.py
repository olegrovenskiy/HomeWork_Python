import os

bash_command = ["cd C:/Users/Lenovo/PycharmProjects/pythonProject/HomeWork_Python/", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print("~/netology/sysadm-homeworks/", prepare_result)


