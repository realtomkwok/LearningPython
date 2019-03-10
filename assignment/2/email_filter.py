
# Author: Junhao Guo

"""
Given a list of random email addresses as follow:
"""
emails =['h#p"f@mg2.org', '3v3#lx@x0h.rfaa', 'yq0k@x0h.rfaa', 'wcd9@nfwb.org', 'm#j@nfwb.org', 'jnib@nfwb.org',
         'ialyi@4ka".kkgh', '4bi@4ka".kkgh', 'g9kcj@4ka".kkgh', 'tj1@ma7.wqv', 'a#m!6n@ma7.wqv', '#jq@ma7.wqv',
         'ro6rf1@ma7.wqv', 'g1t7ij@nfif.sh', 'hvjx7p@2qqu.net', 'uqjdk@2qqu.net', 'svx@2qqu.net', 'rhx2@2qqu.net',
         'hda1@a6!.dgg', 'ng!xjj@a6!.dgg', 'mw5a@nj".org', '88oy@nj".org', '8rvu9z@nj".org', '1jr@nj".org',
         '6bvy@xjh.net', 'n4"cb@xjh.net', 'z1kd@9"kl.nv', '6r5@uqof.com', '8172@px!n.gthc', 'at7b8s@px!n.gthc', 'a#6a6@px!n.gthc']

"""
1. Write a program to filter out the invalid email addresses and put all valid ones in a sorted list:

Expected printed output:
['6bvy@xjh.net', '6r5@uqof.com', 'hvjx7p@2qqu.net', 'jnib@nfwb.org', 'rhx2@2qqu.net',
'svx@2qqu.net', 'uqjdk@2qqu.net', 'wcd9@nfwb.org']


2. Bonus (optional)
Also group the valid addresses by domain names using a dictionary.

Expected printed output:
{'uqof.com': ['6r5'], 'xjh.net': ['6bvy'], 'nfwb.org': ['wcd9', 'jnib'],
'2qqu.net': ['hvjx7p', 'uqjdk', 'svx', 'rhx2']}

"""
import string

mailList = []
invalidList = []

validLabels = ["com", "org", "net"]
invalidCharacters = list(string.punctuation)
invalidCharacters.remove(".")
invalidCharacters.remove("@")

for address in emails:
    localAndHostname, domainLabel = address.split(".")
    if domainLabel in validLabels:
       mailList.append(address)

for address in mailList:
    local, domain = address.split("@")
    localList = list(local)
    domainList = list(domain)
    for localCharacters in localList:
        if localCharacters in invalidCharacters:
              invalidList.append(address)
    for domainCharacters in domainList:
        if domainCharacters in invalidCharacters:
            invalidList.append(address)

validMailList = list(set(mailList).difference(set(invalidList)))
print(validMailList)

#mailDict = {}
#domainList = []

#for address in validMailList:
    local, domain = address.split("@")
    domainList.append(domain)
    mailDict = dict.fromkeys(domainList,local)

#print(mailDict)
