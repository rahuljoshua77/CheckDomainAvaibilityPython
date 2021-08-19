import requests
import os
import whois
#DATA TELEGRAM
token = "ISI TOKEN BOT DARI BOTFATHER"
group_id = "ISI CHAT ID"

#DATA GODEDDY
secret_key = "SECREKEY"
api_key = "API_KEY"

headers = {
    "Authorization": f"sso-key {secret_key}:{api_key}",
    "accept":"application/json"
    }
def broadcast_msg(msg):
    
    to_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={group_id}&text={msg}"
    resp = requests.get(to_url)
    get_data = resp.text
    if "true" in get_data:
        print("[*] Sent succesfully!")
    elif "false" in get_data:
        print("[*] Failed sent!")
    else:
        print("[*] Unkown Error")

def extract_info():
    n = 1
    while True:
        try:
            sleep(2)
            url = f"https://api.ote-godaddy.com/v1/domains/available?domain={domain_input}"
            availability_res = requests.get(url, headers=headers)
            if '"available":true'  in str(availability_res.text):
                if n == 6:
                    break
                else:
                    print("[*] Available, Go Buy!")
                    broadcast_msg("[*] Available, Go Buy!") 
                    n = n+1       
            else:
                print("[*] Not Available!")
                broadcast_msg("[*] Not Available!") 
        except Exception as e:
            print(e)

def main():
    global domain_input
    domain_input = input("[*] Masukin Domain: ")
    clear = domain_input.split(".")
    global get_first
    global get_second
    get_first = clear[0]
    get_second = clear[1]
    extract_info()

main()
 
