import os
import psutil
import re
import platform
from requests import get

class Gettinginfo:


    def __init__(self, recibir_todo):
        self.recibir_todo = str(recibir_todo).lower()

    def get(self):

        # help
        if str(self.recibir_todo) == 'help':
            cmd_dispoinbles = ['Get-info.py [system]', 'Get-info.py [interfaces]', 'Get-info.py [all]', 'Get-info.py [all_brief]', 'Get-info.py [wan]']
            return cmd_dispoinbles

        # list
        elif str(self.recibir_todo) == 'interfaces':
            addrs = psutil.net_if_addrs()
            return addrs.keys()

        # system
        elif str(self.recibir_todo) == 'system':
            var_return = {'Operating system detected:': platform.system() }
            return var_return
        # all
        elif str(self.recibir_todo) == 'all':
            var_list = []
            addrs = psutil.net_if_addrs()

            for x in addrs:
                var_list.append(os.popen('ip addr show '+str(x)+' | grep inet').read())
            return var_list
        # all_brief
        elif str(self.recibir_todo) == 'all_brief':
            addrs = psutil.net_if_addrs()
            list_sav = []
            var_return = {}
            #leemos los valores para cada interfaz y lo guardamos.
            for x in addrs:
                p1 = os.popen('ip addr show '+str(x)+' | grep inet').read()
                nuevo_p1 = p1.splitlines()
                for x in p1.splitlines():
                    list_sav.append(x)

            p1 = re.compile(r'(\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)', re.M)

            linea=[]
            for list_interface in addrs.keys(): #para cada interfaz de del host.
                for valor in list_sav: #para cada línea del output ip addr show all_brief
                    name = (r'\s')+ re.escape(list_interface)
                    p2 = re.compile(name, re.M)
                    res1 = re.search(p2, valor)           
                    if res1:
                        linea.append(valor)

            for x in linea:
                for list_interface2 in addrs.keys():
                    name = (r'\s')+ re.escape(list_interface2)
                    p22 = re.compile(name, re.M)
                    res11 = re.search(p1, x)
                    res12 = re.search(p22, x)
                    if res11 and res12 is not None:
                        var_return.update({res12.group(): res11.group()})

            return var_return #Return dict
        elif str(self.recibir_todo) == 'wan':
            var_return = {'IP WAN detected': str((get('https://api.ipify.org').content).decode("utf-8"))}
            return var_return

        else:
            print("This argument does not exist.\nUse the help to know the arguments")

