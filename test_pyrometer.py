import pyrometer_lumasense
import yaml

# Load config data
with open("config_Parameter.yml", "r") as f:
    config = yaml.safe_load(f)

pyro2 = pyrometer_lumasense.PyrometerLumasense(config["IGAR-6-adv"])
print(pyro2.sample())
print(pyro2.k)