"""Module with fixtures for tests"""
import time
import socket
import sys
import re
import paramiko
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from LoginPage import LoginPage


def pytest_addoption(parser):
    """Addoption"""
    parser.addoption("--ip", action="store", default="127.0.0.1", help="Host IP")
    parser.addoption("--login", action="store", default="root", help="login")
    parser.addoption("--password", action="store", default="sergo", help="password")


def parse_ssh_manager_out(text):
    """ssh response parser"""
    text = str.encode(text)
    text = text.decode('utf8')
    text = text.strip("b' ")
    tag = re.compile(r'\\x(?:[0123456789abcdef]{2,2}|[0123456789abcdef]{4,4})')
    text = tag.sub('', text)
    text = text.split('\\n')
    text.pop()
    return text


def command(cmd, hostname, login, password):
    """ssh command manager with return"""
    buff_size = 2048
    stdout = ""
    stderr = ""
    connect_retry_count = 3
    for _ in range(connect_retry_count):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=hostname, username=login, password=password, port=22, allow_agent=False,
                           look_for_keys=False, timeout=10)
        except (paramiko.AuthenticationException,
                paramiko.BadHostKeyException,
                paramiko.SSHException,
                socket.error,
                Exception) as error:
            print(error)
            time.sleep(10)
        else:
            break
    else:
        sys.exit(1)
    chan = client.get_transport().open_session()
    chan.exec_command(cmd)
    retcode = chan.recv_exit_status()

    while chan.recv_ready():
        try:
            stdout += str(chan.recv(buff_size))
        except TypeError:
            stdout += chan.recv(buff_size)

    while chan.recv_stderr_ready():
        try:
            stderr += str(chan.recv_stderr(buff_size))
        except TypeError:
            stderr += chan.recv_stderr(buff_size)

    client.close()
    return retcode, parse_ssh_manager_out(stdout), parse_ssh_manager_out(stderr)


def command_without_return(cmd, hostname, login, password):
    """ssh command manager without return"""
    connect_retry_count = 3
    for _ in range(connect_retry_count):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=hostname, username=login, password=password, port=22, allow_agent=False,
                           look_for_keys=False, timeout=10)
        except (paramiko.AuthenticationException,
                paramiko.BadHostKeyException,
                paramiko.SSHException,
                socket.error,
                Exception) as error:
            print(error)
            time.sleep(10)
        else:
            break
    else:
        sys.exit(1)
    chan = client.get_transport().open_session()
    chan.exec_command(cmd)
    client.close()


@pytest.fixture
def get_driver(request):
    """Fixture to create, return and close driver"""
    options = Chrome_options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)

    def close_driver():
        driver.quit

    request.addfinalizer(close_driver)
    return driver


@pytest.fixture
def cmdopt_hostname(request):
    """hostname fixture"""
    return request.config.getoption("--ip")


@pytest.fixture
def url(cmdopt_hostname):
    """URL fixture"""
    return "http://" + cmdopt_hostname + "/opencart"


@pytest.fixture
def cmdopt_login(request):
    """Login fixture"""
    return request.config.getoption("--login")


@pytest.fixture
def cmdopt_password(request):
    """Password fixture"""
    return request.config.getoption("--password")


@pytest.fixture
def apache_restart_test(cmdopt_hostname, cmdopt_login, cmdopt_password):
    """Apache restart fixture"""
    command("systemctl restart apache2", cmdopt_hostname, cmdopt_login, cmdopt_password)
    retcode, stdout, stderr = command("systemctl is-active apache2", cmdopt_hostname, cmdopt_login, cmdopt_password)
    current_result = retcode
    expected_result = 0
    return expected_result, current_result


@pytest.fixture
def mysql_restart_test(cmdopt_hostname, cmdopt_login, cmdopt_password):
    """MySQL restart fixture"""
    command("systemctl restart mysql", cmdopt_hostname, cmdopt_login, cmdopt_password)
    retcode, stdout, stderr = command("systemctl is-active mysql", cmdopt_hostname, cmdopt_login, cmdopt_password)
    current_result = retcode
    expected_result = 0
    return expected_result, current_result


@pytest.fixture
def is_base_page(get_driver, url):
    """Check base page fixture"""
    login_page = LoginPage(get_driver, url)
    login_page.navigate()
    current_result = login_page.get_title()
    expected_result = "Your Store"
    return expected_result, current_result


@pytest.fixture
def server_reset(cmdopt_hostname, cmdopt_login, cmdopt_password):
    """Server reset fixture"""
    command_without_return("reboot", cmdopt_hostname, cmdopt_login, cmdopt_password)
