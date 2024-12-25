from discordwebhook import Discord

def notify_to_discord_channel(first_team_name, second_team_name, different_value, current_url, game_time, pre_game_total, current_total, difference_calibrated):
    discord = Discord(url="https://discord.com/api/webhooks/1171739304146509874/ntpE3JBD9ll5QS8Ah-BY3Q8ECK3pSQA6WNW_UClIKI-9elJpIliECigrxYV3SlJqxUAj")
    title = f"💥**{first_team_name}**💥 vs 💥**{second_team_name}**💥"
    message = f":face_with_open_eyes_and_hand_over_mouth:  It is [**{str(different_value)}**]({current_url}) different from the pre game total 👀"
    # discord.post(content=message)
    discord.post(
        username="Watcher",
        avatar_url="https://img.freepik.com/free-vector/basketball-ball-isolated_1284-42545.jpg?w=740&t=st=1699445903~exp=1699446503~hmac=577a11eee3da5efd7a8cd17b51a5896d837165708b389a27a6debb8da8564592",
        # content=title,
        embeds=[
            {
                "author": {
                    "name": "Contact us ☎️ ",
                    "url": "https://www.watcher.com",
                    "icon_url": ""
                },
                "title": title,
                "description": message,
                "thumbnail": {"url": "https://img.freepik.com/free-vector/gradient-basketball-logo-template_23-2149373179.jpg?w=740&t=st=1699446730~exp=1699447330~hmac=beaa2f964db5c9ba2f4805f248e5bc42949e5b9c896b89f78de3b6a5d4a2d8dd"},
                "color": 15258703,
                "url": current_url,
                "fields": [
                    {
                        "name": "",
                        "value": "",
                    },
                    {
                        "name": "Game Time ⏰",
                        "value": str(game_time),
                        "inline": True
                    },
                    {
                        "name": "",
                        "value": "",
                        "inline": True
                    },
                    {
                        "name": "",
                        "value": "",
                        "inline": True
                    },
                    {
                        "name": "Pregame total",
                        "value": str(pre_game_total),
                        "inline": True
                    },
                    {
                        "name": "Current total",
                        "value": str(current_total),
                        "inline": True
                    },
                    {
                        "name": "Difference calibrated",
                        "value": str(difference_calibrated),
                        # "inline": True
                    },
                ],
                "image": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Sky_Sport_NBA_HD_-_Logo_2020.svg/640px-Sky_Sport_NBA_HD_-_Logo_2020.svg.png"
                },
                # "footer": {
                #     "text": "NBA",
                #     "icon_url": "https://api.sofascore.app/api/v1/unique-tournament/132/image"
                # }
            }
        ],
    )

# notify_to_discord_channel("CCC", "BBB", "8", "https://img.freepik.com/", "2023-11-09 02:30", 237.5, 240.5, 5)