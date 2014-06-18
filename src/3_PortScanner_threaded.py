# lib for parsing the arguments given at the launch of the script
import argparse 
# lib for the socket
from socket import *
# lib for the threads
from threading import *

"""
    Port Scanner using threads
    *Notice the use of the semaphore in order to attribute a kind of
    order 
"""

screenLock = Semaphore(value=1)
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
        screenLock.acquire()
        print "[-]%d/tcp closed " %tgtPort
    finally:
        screenLock.release()
        connSkt.close
        
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
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        
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


    if(tgtHost == None) or (tgtPorts == None):
        print "[-] You must specify a target host and port[s]"
        exit(0) 
    # Launch of the program itself
    print tgtHost, tgtPorts
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
