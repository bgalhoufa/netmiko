from netmiko import Netmiko

my_device = {
        'host':'c9300lab',
        'username':'expert',
        'password':'1234QWer!',
        'device_type':'cisco_ios'
        }


net_conn = Netmiko(**my_device)
       
output = net_conn.send_command('show ip arp', use_textfsm=True)        

print(output[0])
        
#print(output)
#print(net_conn.find_prompt())

net_conn.disconnect()
