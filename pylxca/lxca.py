import salt
import sys
import requests
from pylxca.pylxca_cmd.lxca_pyshell import *
# import pylxca
con1 = connect("https://<IP>","<USER>","<PASS>","True")

def hello():
    return "Hello World"

def chassisList():
    chassisList = chassis(con1, status = 'managed')
    return chassisList

def nodeList():
    nodeList = nodes(con1, status = 'managed')
    return nodeList

def userList():
    userList = users(con1)
    return userList

def test():
    return "Test2"

