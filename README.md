# HomeWork_Python

# Домашнее задание 4.2. Использование Python для решения типовых DevOps задач

## Задание 1

  Скрипт

	  #!/usr/bin/env python3
	  a = 1
	  b = '2'
	  c = a + b

 Значение с - будет выдана ошибка, т.к. происходит сложение целого числа со строкой

 TypeError: unsupported operand type(s) for +: 'int' and 'str'

 Для значения с - 12 можем модернизировать скрипт:

	  #!/usr/bin/env python3
  	  a=1
	  b='2'
	  d=str(a)
	  c=d+b
	  print (c)

 Для значения с - 3 можем модернизировать скрипт следующим образом:

	  #!/usr/bin/env python3
	  a=1
	  b='2'
	  d=int(b)
	  c=d+a
	  print (c)

## Задание 2
	
	  #!/usr/bin/env python3

	  import os
	
	  bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
	  result_os = os.popen(' && '.join(bash_command)).read()
	
	  for result in result_os.split('\n'):
  	    if result.find('modified') != -1:
   	       prepare_result = result.replace('\tmodified:   ', '')
   	       print("~/netology/sysadm-homeworks/", prepare_result)
     	   

## Задание 3

	  #!/usr/bin/env python3
	
	  import os

	  directory = str(input("Введите директорию:  "))
	  argument1 = ["cd", directory]
	  argument = (' '.join(argument1))
	  bash_command = [argument, "git status"]
		  result_os = os.popen(' && '.join(bash_command)).read()
		    
		  for result in result_os.split('\n'):
  	 	  if result.find('modified') != -1:
   	   	      prepare_result = result.replace('\tmodified:   ', '')
   	    	      print(argument, prepare_result)
     	   

## Задание 4


  #!/usr/bin/env python3

  print ("hello")
  import socket
  i=0
  oldaddr = ["74.125.131.194", "142.250.150.19", "173.194.220.100"]
  
  urls = ["drive.google.com", "mail.google.com", "google.com"]
  
  while i<3:
  
          ipaddr = socket.gethostbyname(urls[i])
          if ipaddr != oldaddr[i]:
                 print ("[ERROR]", urls[i], " IP mismatch:"," старый IP-",oldaddr[i], "Новый IP-",ipaddr)
          print (urls[i], ipaddr)
          i=i+1







