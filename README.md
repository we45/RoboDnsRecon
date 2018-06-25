## RoboDnsRecon

Robot Framework Library for DNS-Recon

**Supports Python 2.7.x for now**

### Install Instructions
* You need docker to run this program
* Pull the DNS Recon docker image: `docker pull we45/dnsrecon`


### Keywords

`run dnsrecon`

`| run dnsrecon  | results path  | domain  | dns  | enumeration type  | sub domain wordlist`

* results path: where your results will be stored. An `.xml` file and  `.json` file are generated as outputs
* domain : Target domain.
* dns (optional): DNS to be used. Default = 8.8.8.8
* enumeration type (optional): Type of enumeration to perform. Default = std
* sub domain wordlist (optional): File with sub-domain and hostnames to use for brute force. Default = None