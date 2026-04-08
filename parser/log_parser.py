import pandas as pd
import re
from datetime import datetime


def parse_auth_log(file_path):
    data = []

    # Regex auth.log standard format:
    # Jul 10 10:15:32 hostname sshd[1234]: Failed password for root from 192.168.1.10 port 22 ssh2
    pattern = re.compile(
    r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+).*Failed password for (?:invalid user )?(\w+) from ([\d\.]+)'
    )

    success_pattern = re.compile(
    r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+).*Accepted password for (\w+) from ([\d\.]+)'
    )

    with open(file_path, "r") as file:
        for line in file:
            match = pattern.search(line)
            success_match = success_pattern.search(line)
            if match:
                timestamp = match.group(1)
                hostname = match.group(2)
                user = match.group(3)
                ip = match.group(4)

                data.append([
                    timestamp,
                    hostname,
                    user,
                    ip,
                    "FAILED_LOGIN"
                ])
            if success_match:
                timestamp = success_match.group(1)
                hostname = success_match.group(2)
                user = success_match.group(3)
                ip = success_match.group(4)

                data.append([timestamp, hostname, user, ip, "SUCCESS_LOGIN"])

    df = pd.DataFrame(
        data,
        columns=["timestamp", "hostname", "user", "ip", "event"]
    )

    current_year = datetime.now().year

    df["timestamp"] = pd.to_datetime(
        df["timestamp"] + f" {current_year}",
        format="%b %d %H:%M:%S %Y"
    )

    return df
