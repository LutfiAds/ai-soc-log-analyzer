import os
import pandas as pd
from parser.log_parser import parse_auth_log


def load_multiple_auth_logs(directory):

    all_dataframes = []

    for filename in os.listdir(directory):

        if filename.endswith(".log"):

            file_path = os.path.join(directory, filename)

            df = parse_auth_log(file_path)

            # fallback hostname dari filename kalau parser gagal ambil hostname
            if "hostname" not in df.columns or df["hostname"].isnull().all():

                hostname = filename.replace("_auth.log", "")

                df["hostname"] = hostname

            all_dataframes.append(df)

    if not all_dataframes:
        return pd.DataFrame()

    combined_df = pd.concat(all_dataframes, ignore_index=True)

    return combined_df
