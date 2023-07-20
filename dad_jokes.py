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

def whatsapp_send_mssg():
    pw.sendwhatmsg("+916379503451",get_dad_joke(),time_hour= 17,time_min= 39)
    # pw.sendwhatmsg_to_group(group_id="BSi2ZxNGOsWA81LUADwuJS",message= get_dad_joke(),time_hour = 15,time_min= 50)


if __name__ == "__main__":
    whatsapp_send_mssg()
