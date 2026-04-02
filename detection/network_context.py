import yaml
import ipaddress


def load_trusted_subnets(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return [ipaddress.ip_network(subnet) for subnet in config["trusted_subnets"]]


def check_trusted_ip(ip, trusted_subnets):
    ip_obj = ipaddress.ip_address(ip)

    return any(ip_obj in subnet for subnet in trusted_subnets)


def apply_network_context(df, config_path):

    trusted_subnets = load_trusted_subnets(config_path)

    df = df.copy()

    df["trusted_network"] = df["ip"].apply(
        lambda x: check_trusted_ip(x, trusted_subnets)
    )

    return df
