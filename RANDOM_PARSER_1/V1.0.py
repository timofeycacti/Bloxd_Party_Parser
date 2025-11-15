from string import ascii_uppercase

import colorama
import requests
import json
from colorama import Fore, init
import random
from time import sleep as s

# All the things, that can be changing are marked (And the errors with them)

colorama.init()
starterName="WittyLion" # Your account name start
letters=list(ascii_uppercase)+list(range(1,9))

url = "https://social7.bloxd.io/social/join-party" # It can be social14 and, i think much more. Look in the headers in your browser, error 400
def gen_payload(partyCode: str):
    return {"metricsCookies":{"3PAPISID":"N/A","1PAPISID":"N/A","3PSID":"N/A","1PSID":"N/A","3PSIDMC":"GW_g4EdClrM-7nPd7MOyeXIRPaN8SgPl9RDDIoapqmyZFJbDD6LoxWuGCucS7n_Sz4CCzQ2Q9lnR63S3aovEDzNjGvRFkF5V4Quurp_vhK5ziNOksoz5iU-DLPv5KCc923jBpB5xArG0Vhtg5gHQ3Shw2wSKv7pAumXWND7AEv5HbAgZ8GExFLBcd6xPcu-udF0lS9inAdv5Cpv48vsRAXgkXNpsf-gxKOUggxwHcGRgXVSr0aqIWsC3cp","3PSIDMCPP":"ztJ9nmiMPMJ36O6FRM37314CiB3l3XUf8BJb.ztJUTB3l3yHKHey76KECTm2PncpOHQFOHfJ_dM373eV_Im96zfgy3rvM56Cqdyysd_8d3MwMie8FIQytTfsNie8yneFUTY9c3rUci18yABJUTYC-ie8OLfgBHfsyTh_-Tm8tHf4UnYaMPeT9nNsyABJXZfsrnKJX6Ys-im6MP17MTK8Unm4JTNRMPy2IjLwMie8FIQytTfshZfsrnKJX5QscZfTUINXMPeT9nNsyABJUHf5MPrhKsrRtRS3FRrh73e8aiB3lRdiYRO3wsditRLwMHf8X3rvMHeF-zm5kHYFUTQCc3MwMZfsO3rvMHeF-zm5kHfgU3MwMiK8M3rvMHeF-zm5kHYFUTQCc31c.F8l7k9vucif9k9dGXBvjTqB65nfGznIH7sm0zb4TpgDkG9JaPDZyZxoPGMLY8RlHYpd9Snm-dpDvUuUUMg5NPk","3PSIDMCSP":"0j0f03K6J009m11000000j0010s17wILM90p0q000R00tsw10B000J01bW71"},"contents":{"partyCode":partyCode}}


headers = {
    "accept": "application/json",
    "accept-language": "en-GB,en;q=0.9,ru;q=0.8,en-US;q=0.7,de;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://bloxd.io/"
}



possible=[]
try:
    for i in range(100):
        l=random.choice(letters)
        l2=random.choice(letters)
        l3=random.choice(letters)
        party_to_request="".join(map(str,[l,l2,l3]))
        # party_to_request="1XD"
        response = requests.post(url, json=gen_payload(party_to_request), headers=headers, timeout=10)
        if response.status_code == 420:
            print(Fore.RED+"Request limit reached! [420 error]") # Just update the tokens to new in payload (Error 420)
            quit()
        elif response.status_code == 200:
            print(Fore.GREEN+f"Successfully joined party {party_to_request}")
            possible.append(party_to_request)
            if not response.json()["leaderSocialPreview"]["name"].startswith(starterName):
                with open("./Bloxd_Parsed_Parties.json","a") as filet:
                    filet.write(f"PartyCode: {party_to_request} \nLeader Name: {response.json()['leaderSocialPreview']['name']}\n\n\n")
                print(Fore.MAGENTA + f"Party {party_to_request} is not empty!")
                print(response.json())
        elif response.status_code == 400:
            print(Fore.LIGHTRED_EX+f"Not found party {party_to_request}")
        elif response.status_code == 401:
            print(Fore.RED+"Wrong tokens! [401 Unathorized Error]")
            quit()
        else:
            print(response)
        s(1)

except KeyboardInterrupt:
    print(Fore.LIGHTYELLOW_EX+"STOPPED")
with open("ALLOWED.txt", "a") as f:
    f.write("\n".join(possible))
