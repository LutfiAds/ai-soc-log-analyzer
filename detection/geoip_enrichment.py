import geoip2.database
import ipaddress


def enrich_geoip(df, db_path):

    reader = geoip2.database.Reader(db_path)

    df = df.copy()

    def get_country(ip):
        try:
            ip_obj = ipaddress.ip_address(ip)

            if ip_obj.is_private:
                return "Internal Network"

            response = reader.city(ip)
            return response.country.name

        except:
            return "Unknown External"

    df["country"] = df["ip"].apply(get_country)

    return df
