# performs scan with the tool nmap
import nmap
# lib for parsing the arguments given at the launch of the script
import argparse

"""
    Port scanner with nmap


"""

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print "[*] "+ tgtHost +"tcp/"+ tgtPort +" "+state


def main():
    """
        Takes the arguments and launches the function portScan, if
        the args are given.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', help='A host(number or figure)')
    parser.add_argument('-p', help='A list of ports to be scanned')

    args=parser.parse_args()
    tgtHost = args.H
    tgtPorts = args.p

    if(tgtHost == None) or (tgtPorts == None):
        print "[-] You must specify a target host and port[s]"
        exit(0)
    # Launch of the program itself
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()
