import ipaddress
import random

for i in range(50):
    gennet = random.randint(0x0b000000, 0xdf000000)
    genmask = random.randint(8, 24)
    randomnet = ipaddress.IPv4Network((gennet, genmask), strict=False)
    print(randomnet)