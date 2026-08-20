# Домашнее задание к занятию "Кластеризация и балансировка нагрузки" - Кошелев Дмитрий


### Инструкция по выполнению домашнего задания

   1. Сделайте `fork` данного репозитория к себе в Github и переименуйте его по названию или номеру занятия, например, https://github.com/имя-вашего-репозитория/git-hw или  https://github.com/имя-вашего-репозитория/7-1-ansible-hw).
   2. Выполните клонирование данного репозитория к себе на ПК с помощью команды `git clone`.
   3. Выполните домашнее задание и заполните у себя локально этот файл README.md:
      - впишите вверху название занятия и вашу фамилию и имя
      - в каждом задании добавьте решение в требуемом виде (текст/код/скриншоты/ссылка)
      - для корректного добавления скриншотов воспользуйтесь [инструкцией "Как вставить скриншот в шаблон с решением](https://github.com/netology-code/sys-pattern-homework/blob/main/screen-instruction.md)
      - при оформлении используйте возможности языка разметки md (коротко об этом можно посмотреть в [инструкции  по MarkDown](https://github.com/netology-code/sys-pattern-homework/blob/main/md-instruction.md))
   4. После завершения работы над домашним заданием сделайте коммит (`git commit -m "comment"`) и отправьте его на Github (`git push origin`);
   5. В личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем Github.
   6. Любые вопросы по выполнению заданий спрашивайте в разделе “Вопросы по заданию” в личном кабинете.
   
Желаем успехов в выполнении домашнего задания!
   
### Дополнительные материалы, которые могут быть полезны для выполнения задания

1. [Руководство по оформлению Markdown файлов](https://gist.github.com/Jekins/2bf2d0638163f1294637#Code)

---

### Задание 1

ЗАДАНИЕ 1: Round-robin на 4 уровне
-----------------------------------
2 Python сервера запущены на портах 8001 и 8002
HAProxy настроен на порту 8080 с балансировкой Round-robin
Запросы распределяются по очереди между серверами


global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend http-frontend
    bind *:8080
    mode http
    # Проверяем Host заголовок
    acl is_example_local hdr(host) -i example.local
    use_backend weighted-servers if is_example_local
    # Если не example.local - возвращаем ошибку или перенаправляем
    default_backend no-match

backend weighted-servers
    mode http
    balance roundrobin
    # Веса: server1 - 2, server2 - 3, server3 - 4
    # HAProxy использует параметр weight
    server server1 127.0.0.1:8001 check weight 2
    server server2 127.0.0.1:8002 check weight 3
    server server3 127.0.0.1:8003 check weight 4

backend no-match
    mode http
    http-request deny deny_status 403
    # Или можно вернуть сообщение
    # http-request return status 403 content-type text/plain string "Access denied: domain example.local required"

Скриншоты:
![Задание 1](./img/1.2.png);
![Задание 1](./img/1.3.png);
![Задание 1](./img/1.4.png);
![Задание 1](./img/1.png);




---

ЗАДАНИЕ 2: Weighted Round Robin на 7 уровне
--------------------------------------------
3 Python сервера запущены на портах 8001, 8002, 8003
Настроены веса: Server1 - 2, Server2 - 3, Server3 - 4
Балансировка работает только для домена example.local
Запросы без домена example.local блокируются (403 Forbidden)

global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend http-frontend
    bind *:8080
    mode http
    acl is_example_local hdr(host) -i example.local
    use_backend weighted-servers if is_example_local
    default_backend no-match

backend weighted-servers
    mode http
    balance roundrobin
    server server1 127.0.0.1:8001 check weight 2
    server server2 127.0.0.1:8002 check weight 3
    server server3 127.0.0.1:8003 check weight 4

backend no-match
    mode http
    http-request deny deny_status 403

listen stats
    bind *:8081
    mode http
    stats enable
    stats uri /stats
    stats refresh 10s
    stats auth admin:admin
	
Скриншоты:
![Задание 1](./img/2.png);
![Задание 1](./img/3.png);
![Задание 1](./img/4.png);
![Задание 1](./img/5.png);
![Задание 1](./img/6.png);
![Задание 1](./img/7.png);
![Задание 1](./img/8.png);
![Задание 1](./img/9.png);





---

### Задание 3

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота](ссылка на скриншот)`

### Задание 4

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота](ссылка на скриншот)`
