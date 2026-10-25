<!-- gemini-3.5-flash-lite (Gemini, 2-й читатель), mastering_openvpn_06.txt -->
### Проверка подключения · Убедитесь, что сервер доступен по сети и корректно отдает информацию, прежде чем подключать клиент (например, через `ldapsearch` для LDAP). · `Make sure this is working before attempting to connect an OpenVPN client.` · (стр. 184)

### Отладка авторизации · Увеличьте уровень логирования до `verb 5` на сервере и следите за логами при ошибках подключения. · `Add the following line to the bottom of the configuration file and restart the server: verb 5` · (стр. 184)

### Устранение проблем с файобрусом (Windows) · Создавайте правила брандмауэра по принципу «первого совпадения» (first-match): обработка правил прекращается сразу при первом совпадении с пакетом. · `Windows Firewall with Advanced Security is a first-match firewall type. This means that as soon as a firewall rule matches a given network packet, processing of the ruleset stops...` · (стр. 196)
