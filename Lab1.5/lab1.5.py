import glob
setips = set()
for txtfile in glob.glob("*.txt"):
    with open(txtfile) as a:
        for line in a:
            if line.find("ip address") == 1:
                setips.add(line.replace("ip address", "").strip())
for i in setips:
    print(i)