import ipaddress
def port_name(number):
    if number >= 0 and number <= 1023:
        return 'Well-known port'
    if number >= 1024 and number <= 49151:
        return 'Registered port'
    if number >= 49152 and number <= 65535:
        return 'Dynamic port'

with open("C:\\Users\\bhuvi\\Desktop\\Interview\\file\\problem_input.txt", 'r') as ip_file:
    for line in ip_file:
        # distinguishing between subnet and port
        if '/' in line:
            # creating a IPv4 network with the given subnet
            addr = ipaddress.IPv4Network(line.strip(), False)
            print(addr[1], addr[-1])
        if ':' in line:
            idx = line.rfind(':')
            prefix = line[:idx]
            # seperating the IP address and the port
            number = int(line[idx+1:].strip())
            print(prefix, port_name(number))

