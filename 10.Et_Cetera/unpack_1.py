def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# * to unpack a list
print(total(*coins), "Knuts")

coinsdict = {
    "galleons": 100,
    "sickles": 50,
    "knuts": 25
}

# ** to unpack a dictionary
print(total(**coinsdict), "Knuts")