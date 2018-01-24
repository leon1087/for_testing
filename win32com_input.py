import pythoncom
import win32com.client

def login(username, password):
	shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(username)
    shell.Sendkeys("{TAB}")
    shell.Sendkeys(password)
    shell.Sendkeys("{ENTER}")