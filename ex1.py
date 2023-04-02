from netmiko import Netmiko

my_device = {
        'host':'c9300lab',
        'username':'expert',
        'password':'1234QWer!',
        'device_type':'cisco_ios'
        }

net_conn = Netmiko(**my_device)
       
#config_set = ['no vlan 2555', 'no int vlan 2555']

#output = net_conn.send_config_from_file('config_set.txt')

#output = net_conn.send_command_timing('copy run start') 
#output = net_conn.send_config_set(config_set) 

#if 'confirm' in output:
#    output += net_conn.send_command_timing('\n')

output = net_conn.send_command('show ip int brief | i up', use_textfsm=True)

print(output)
