import argparse
from socket import *


def connScan(tgtHost, tgtPort):
    """
        Try to connect with the socket library, to
        a host, with a host & port given in the
        arguments
        Print and close the socket
    """
    try:
        connSocket = Socket(AF_INET, SOCK_STREAM)
        connSocket.connect((tgtHost, tgtPort))
        connSocket.send('ViolentPython\r\n')
        results = connSocket.recv(100)
        print "[+]%d/tcp open " %tgtPort
        print "[+] "+ str(results)
        connSocket.close()
    except:
        print "[-]%d/tcp closed " %tgtPort
        
def portScan(tgtHost, tgtPorts):
    """
        Given a host, and a list of ports to look into,
        this function scans all the ports of the given host,
        and print the resultats        
    """
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve %s: Unknown host" %tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print "\n[+] Scan Results for:" + tgtName[0]
    except:
        print "\n[+] Scan Results for: "+ tgtIP

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port '+ tgtPort
        connScan(tgtHost, int(tgtPort))
        
def main():
    """
        Takes the arguments and launches the function portScan, if
        the args are given.
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', help='A host(number or figure)')
    parser.add_argument('-p', help='A list of ports to be scanned',nargs='+')
    
    args=parser.parse_args()
    tgtHost = args.H
    tgtPorts = args.p


    if(tgtHost == None) and (tgtPorts == None):
        print "[-] You must specify a target host and port[s]"
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
