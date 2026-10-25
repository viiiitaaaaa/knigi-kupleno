<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), mastering_openvpn_03.txt -->
### Проверка работоспособности туннеля по логам · Проверяйте лог-файлы OpenVPN на обоих концах соединения на наличие ключевой фразы успешной инициализации (`Initialization Sequence Completed`). · `Check the openvpn.log files on both ends for the magic sentence: Thu Sep 11 15:57:51 2014 Initialization Sequence Completed` · (стр. 71)

### Права доступа к скриптам · Убедитесь, что кастомные скрипты (`up.sh`) имеют права на выполнение перед запуском VPN-соединения. · `Make sure the up.sh scripts are executable (chmod a+x up.sh) before starting the VPN connection.` · (стр. 70)

### Защита от потери трафика при сбое · Используйте задержку добавления маршрутов (`route-delay`), чтобы маршруты добавлялись только после полной доступности всех соединений. · `The configuration statement route-delay is required here to ensure that the routes are added after all connections are available.` · (стр. 76)

### Использование полного имени сетевого интерфейса · При настройке моста всегда указывайте полное имя tap-устройства с цифрой (например, `dev tap0`), иначе OpenVPN откроет новое устройство, и мост не заработает. · `In the configuration file, the full name of the device tap0 is used. If the 0 is omitted, then OpenVPN will open a new tap adapter and the bridge will not function.` · (стр. 79)

### Безопасность инфраструктуры ключей (PFS) · Используйте X.509 сертификаты и приватные ключи вместо пре-shared ключей для обеспечения Perfect Forwarding Secrecy (PFS), что защищает ранее записанный трафик от расшифровки при компрометации ключей. · `The advantage of using X.509 certificates over pre-shared keys is that it offers Perfect Forwarding Secrecy (PFS)... With PFS, it is not possible to decrypt old data.` · (стр. 81)

### Опасность удаления каталога Easy-RSA · При инициализации Easy-RSA всё содержимое указанной директории (`EASYRSA`) будет удалено; будьте осторожны при задании этого пути, так как там хранится хранилище сертификатов. · `When Easy-RSA is initialized, everything within the EASYRSA directory will be deleted. Be careful about what you define here.` · (стр. 91)

### Ограничения Common Name в Easy-RSA · Не используйте пробелы в поле Common Name (CN), так как это вызовет проблемы в Easy-RSA, а также с CCD и директивой `common-name-as-username`. · `Spaces should not be used in the Common Name field. This will cause problems in Easy-RSA as well as potentially with CCDs...` · (стр. 92)

### Предварительное создание CRL · Всегда генерируйте пустой файл CRL (`gen-crl`), чтобы настроить конфигурацию OpenVPN заранее и избежать ошибок об отсутствии файла в логах. · `...it is recommended to generate an empty CRL. This allows you to stage your OpenVPN configuration with the file, and will not require a restart later.` · (стр. 94)
