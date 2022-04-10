import re
import subprocess

class WifiPassword: 

    def __init__(self,dir):
        self.dir = dir
        self.wifi_list = []

    def decode(self,outputs): 
        results = []
        outputs = str(outputs).split('\n')
        for output in outputs: 
            output = output.split(":")
            if len(output) > 1 and output[1] != ' ': 
                results.append(output[0].strip())
                results.append(output[1].strip())
        return results

    def run(self): 
        outputs = subprocess.getoutput("netsh wlan show profiles")
        profile_names = self.decode(outputs)[1::2]

        if len(profile_names) != 0:
            for profile_name in profile_names:

                wifi = {
                    "name": profile_name,
                    "password": "none"
                }

                outputs = subprocess.getoutput("netsh wlan show profile " + profile_name + " key=clear")
                wifi_infos = self.decode(outputs)
                for i in range(0, len(wifi_infos) -1): 
                    try: 
                        if wifi_infos[i] == "Key Content" or wifi_infos[i] == "关键内容": 
                            wifi["password"] = wifi_infos[i+1]
                    except: 
                        break
                # print(wifi)
                self.wifi_list.append(wifi)
        self.write_file()

    def write_file(self): 
        with open(self.dir + '\wifi.txt', 'w') as f:
            for wifi in self.wifi_list:
                f.write("%s\n" % wifi)
