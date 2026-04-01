import pandas as pd
import re


def parse_auth_log(file_path):
    data = []

    pattern = re.compile(
        r'(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (\w+) from ([\d\.]+)'
    )

    with open(file_path, "r") as file:
        for line in file:
            match = pattern.search(line)

            if match:
                timestamp = match.group(1)
                user = match.group(2)
                ip = match.group(3)

                data.append([timestamp, user, ip, "FAILED_LOGIN"])

    df = pd.DataFrame(data, columns=["timestamp", "user", "ip", "event"])

    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%b %d %H:%M:%S")

    return df
