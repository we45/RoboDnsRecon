import docker
from robot.api import logger
from docker.types import Mount

class RoboDnsRecon(object):

    def __init__(self):
        self.client = docker.from_env()
        self.dsnrecon_docker = "we45/dnsrecon"


    def run_dnsrecon(self, results_path, domain, dns='8.8.8.8', enumeration_type='std', sub_domain_wordlist='None'):
        self.results_path = results_path
        self.domain = domain
        self.dns = dns
        self.enumeration_type = enumeration_type
        self.sub_domain_wordlist = sub_domain_wordlist
        results_mount = Mount("/dnsrecon_results", self.results_path, type="bind")
        if sub_domain_wordlist != 'None':
            self.sub_domain_wordlist = sub_domain_wordlist
            sub_domain_wordlist_file = self.sub_domain_wordlist.split('/')[-1]
            sub_domain_wordlist_mount = Mount("/{0}".format(sub_domain_wordlist_file), self.sub_domain_wordlist, type="bind")
            mounts = [results_mount, sub_domain_wordlist_mount]
            command = '-d {0} -D /{1} -t {2} --json /dnsrecon_results/dnsrecon_{3}_results.json --xml /dnsrecon_results/dnsrecon_{4}_results.xml'.format(self.domain, sub_domain_wordlist_file, self.enumeration_type, self.domain, self.domain)
        else:
            mounts = [results_mount]
            command = '-d {0} -t {1} --json /dnsrecon_results/dnsrecon_{2}_results.json --xml /dnsrecon_results/dnsrecon_{3}_results.xml'.format(self.domain, self.enumeration_type, self.domain, self.domain)
        self.dns = [str(self.dns)]
        self.client.containers.run(self.dsnrecon_docker, mounts=mounts, dns=self.dns, command=command)
        logger.info("Successfully ran DNS-Recon against the target domain {0}. Please find the *.json and *.xml files in the results directory".format(self.domain))
