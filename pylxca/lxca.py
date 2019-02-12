# Basic implementation of the PyLXCA functions listed at
# https://sysmgt.lenovofiles.com/help/topic/com.lenovo.lxca.doc/pycli_reference.html?cp=1_21_1_2

# ToDo - CLI options, such as IP/User/Pass, and other parameters
# May need ostream() to set output stream, but prob not

import salt
import sys
import requests
from pylxca.pylxca_cmd.lxca_pyshell import *
# import pylxca
con1 = connect("https://<IP>","<USER>","<PASS>","True")

### General -- Are any of these necessary as functions?  Prob not.
# connect, disconnect, exit, help, ostream

### Device Management -- Also probably unnecessary?
# discover, manage, unmanage

### Inventory
# chassis, cmms, fanmuxes, fans, nodes, powersupplies, scalablesystem, switches

def chassisList():
    chassisList = chassis(con1, status = 'managed')
    return chassisList

def cmmsList():
    cmmsList = cmms(con1)
    return cmmsList

def fanmuxesList():
    fanmuxesList = fanmuxes(con1)
    return fanmuxesList
    
def fansList():
    fansList = fans(con1)
    return fansList
    
def nodeList():
    nodeList = nodes(con1, status = 'managed')
    return nodeList

def powersuppliesList():
    powersuppliesList = powersupplies(con1)
    return powersuppliesList
    
def scalablesystemList():
    scalablesystemList = scalablesystem(con1)
    return scalablesystemList
    
def switchesList():
    switchesList = switches(con1)
    return switchesList
    
### Server Configuration
# configpatterns (UUID), configprofiles (UUID), configtargets (Parameters?)

def configpatternsList():
    configpatternsList = configpatterns(con1)
    return configpatternsList

def configprofilesList():
    configprofilesList = configprofiles(con1)
    return configprofilesList

def configtargetsList(): # Needs additional parameters
    configtargetsList = configtargets(con1)
    return configtargetsList

### Firmware Updates
# updatecomp, updatepolicy, updaterepo (Parameters?)

def updatecompList():
    updatecompList = updatecomp(con1)
    return updatecompList

def updatepolicyList():
    updatepolicyList = updatepolicy(con1)
    return updatepolicyList

def updaterepoList(): # Needs additional parameters
    updaterepoList = updaterepo(con1)
    return updaterepoList

### User Management
# users, storedcredentials

def userList():
    userList = users(con1)
    return userList

def storedcredentialsList():
    storedcredentialsList = storedcredentials(con1)
    return storedcredentialsList

### Service and Support
# fddc (UUID)

def fddcList():
    fddcList = fddc(con1)
    return fddcList

### Logs
# jobs, log, lxcalog, tasks

def jobList():
    jobList = jobs(con1)
    return jobList

def logList():
    logList = log(con1)
    return logList

def lxcalogList():
    lxcalogList = lxcalog(con1)
    return lxcalogList

def taskList():
    taskList = tasks(con1)
    return taskList

### Non-LXCA Testing

def hello():
    return "Hello World"

def test():
    return "Test2"

# ToDo - Disconnect String - Is it necessary?

