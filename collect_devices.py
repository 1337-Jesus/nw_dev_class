class NETWORK_DEVICES:
	device_counter = 0 #class variable that defines number of devices in class
	def __init__(self, name, vendor, function, mgmt_ip):
		self.name = name
		self.vendor = vendor
		self.function = function
		self.mgmt_ip = mgmt_ip
		NETWORK_DEVICES.device_counter += 1 #class variable gets altered
	def remove(self, name):
		print('You have removed {0}'.format(self.name))
		NETWORK_DEVICES.device_counter -= 1 #class variable gets altered


class FIREWALL(NETWORK_DEVICES):
	def __init__(self, name, vendor, function, mgmt_ip, vdom)
		NETWORK_DEVICES.__init__(self, name, vendor, function, mgmt_ip)
		self.vdom = vdom

class SWITCH(NETWORK_DEVICES):
	def __init__(self, name, vendor, function, mgmt_ip, ports)
		NETWORK_DEVICES.__init__(self, name, vendor, function, mgmt_ip)
		self.ports = ports

dev1 = NETWORK_DEVICES('core_hungen_1', 'cisco', 'switch', '10.255.7.130')
dev2 = NETWORK_DEVICES('core_hungen_2', 'cisco', 'switch', '10.255.7.131')
dev3 = NETWORK_DEVICES('fw_hungen', 'fortigate', 'firewall', '10.255.7.129')
 
