import main as m
# @main.check_for_updates(1, "Update!", "https://discord.com/api/webhooks/1066438058376974396/qSoY0VHorM1-bkFbZrOZIdGKIh7h7XobKE21dwqejV2dgNlR2OL0G5o_KRGLmpTrU77z", True)
import os

USERNAME = "BBernYY"
WEBHOOK_TITLE = "Update!"
API_KEY = os.getenv("API_KEY")
INTERVAL = 1
TOGGLE_CHANGE = True
WEBHOOK_URL = os.getenv("WEBHOOK_URL")



def find_uuid_by_name(name):
    from requests import get
    import time
    success = False
    while not success:
        try:
            uuid = get("https://api.mojang.com/users/profiles/minecraft/"+name).json()['id']
        except KeyError:
            success = False
            time.sleep(INTERVAL)
    return uuid

def find_name_by_uuid(uuid):
    from requests import get
    name = get("https://playerdb.co/api/player/minecraft/"+uuid).json()["data"]["player"]["username"]
    return name


def obtain_data(api_key, uuid):
    from requests import get
    request = get("https://api.hypixel.net/status", {
        "key": api_key,
        "uuid": uuid
    }).json()
    return request


def handle_data(data):
    from discord_webhook import DiscordEmbed
    if data["session"]["online"]:
        embed = DiscordEmbed(WEBHOOK_TITLE, description="", color="00ff00")
        new_data = {
            "Game": data["session"]["gameType"],
            "Mode": data["session"]["mode"],
            "%/info/%": {"embed": DiscordEmbed(WEBHOOK_TITLE, description="", color="00ff00")}
        }
    else:
        new_data = {
            "Game": "Offline",
            "Mode": "Offline",
            "%/info/%": {"embed": DiscordEmbed(WEBHOOK_TITLE, description="", color="ff0000")}
        }
    return new_data


def main(name, api_key, interval, show_change, webhook_url):
    @m.check_for_updates(interval, webhook_url, show_change)
    def func():
        data = obtain_data(api_key, find_uuid_by_name(name))
        return handle_data(data)


if __name__ == "__main__":
    main(USERNAME, API_KEY, INTERVAL, TOGGLE_CHANGE, WEBHOOK_URL)
