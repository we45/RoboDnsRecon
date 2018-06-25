*** Settings ***
Library  RoboDnsRecon
Library  Collections

*** Variables ***
${DOMAIN}  example.com
${RESULTS_PATH}  /Users/nithinjois/Downloads/dns_recon_report/
${SUBDOMAIN_WORD_LIST}  /Users/nithinjois/Desktop/RoboDnsRecon/dnsmap.txt
${DNS}  8.8.8.8
${ENUMERATION_TYPE}  std

*** Test Cases ***
RUN DNS RECON
    run dnsrecon  ${RESULTS_PATH}  ${DOMAIN}  ${DNS}  ${ENUMERATION_TYPE}  ${SUBDOMAIN_WORD_LIST}
