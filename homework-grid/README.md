pytest --url=http://demo23.opencart.pro/admin --browser_type={"ie", "firefox", "chrome"} --window_option={"window", "headless"} --waits=waits --wait_time=10 test_lesson_15.py

pytest --url=http://demo23.opencart.pro/admin --browser_type=firefox test_lesson_15.py

java -jar selenium-server-standalone-3.141.59.jar -role hub

java -jar .\selenium-server-standalone-3.141.59.jar -role node -nodeConfig nodeconfig.json