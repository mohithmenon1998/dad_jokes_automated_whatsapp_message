import requests
import pywhatkit as pw


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "text/plain"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke = response.text
        print(joke)
        return joke
    else:
        print(f"Failed to fetch joke. Status code: {response.status_code}")

def whatsapp_send_mssg(mob_no,time):
    if "+91" not in mob_no:
        mob_no = "+91"+mob_no
    t_split= time.split(":")
    hour = int(t_split[0])
    minute =int (t_split[1])
    pw.sendwhatmsg(str(mob_no),get_dad_joke(),hour,minute)
