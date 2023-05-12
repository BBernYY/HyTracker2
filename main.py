def convert_time(t):
    time_spent = (t).seconds
    h = (time_spent - time_spent % 3600) // 3600
    m = (time_spent - time_spent % 60 - h*3600) // 60
    s = (time_spent - h*3600 - m*60)

    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"
    

def generate_description(update2, changes):
    description = ""
    for k, v1 in changes.items():
        v2 = update2[k]
        description += f"The `{k}` changed from `{v1}` to `{v2}`, "
    description = description[:-2]+"."
    return description


    


def send_webhook(embed, url, data, time_elapsed, changes=None):
    from discord_webhook import DiscordWebhook, DiscordEmbed
    webhook = DiscordWebhook(url=url)
    if embed.description == "" and changes:
        embed.description = generate_description(data, changes)
    for k, v in data.items():
        if (k in changes) if changes else False:
            embed.add_embed_field(name="Previous "+k, value=f"`{changes[k]}`", inline=True)
        embed.add_embed_field(name=k, value=f"`{v}`", inline=(True if k in changes else False) if changes else False)
        embed.add_embed_field(name="", value="", inline=False)

    if changes:
        embed.add_embed_field(name="Time Elapsed", value=f"`{convert_time(time_elapsed)}`", inline=True)
    embed.set_footer(text="Programmed by BBernYY on GitHub.", icon_url="https://avatars.githubusercontent.com/u/66414852?s=48&v=4")
    webhook.add_embed(embed)
    response = webhook.execute()

def removed_key(dictionary, key):
    out = dict(dictionary)
    out.pop(key)
    return out



def check_for_updates(interval_seconds, url, show_changes):
    def decorator(func):
        import time
        from datetime import datetime
        update1 = func()
        time1 = datetime.now()
        while True:
            update2 = func()
            changes = {}
            for k, v1 in update1.items():
                if k == "%/info/%":
                    continue
                v2 = update2[k]
                if v1 != v2:
                    changes[k] = v1
            if changes != {}:
                time2 = datetime.now()
                send_webhook(url=url, data=removed_key(update2, "%/info/%"), time_elapsed=time2-time1, changes=changes if show_changes else None, **update2["%/info/%"])
                time1 = datetime.now()

            update1 = dict(update2) # this is so the values dont tangle
            time.sleep(interval_seconds)
    return decorator

def main(): # OUTDATED! USE HYPIXEL.PY !!!
    import random
    @check_for_updates(1, "Update!", "https://discord.com/api/webhooks/1066438058376974396/qSoY0VHorM1-bkFbZrOZIdGKIh7h7XobKE21dwqejV2dgNlR2OL0G5o_KRGLmpTrU77z", True)
    def func():
        r1, r2 = random.random(), random.random()
        return({"test1": 1 if r1 > 0.5 else 0, "test2": 0 if r2 > 0.5 else 1})
        # return({"test1": 1, "test2": 0})
    

if __name__ == "__main__":
    main()