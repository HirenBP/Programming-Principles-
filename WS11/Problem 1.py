# Define a class that simulates a DNS
class DNS:

    def __init__(self):
        self.data = {}
    def update(self, domain, ipa):
        self.data[domain] = ipa
    def lookup(self, domain):
        return self.data.get(domain, None)

dns = DNS()
while True:

    command = input("? ")

    words = command.split()

    if not words:

        continue

    keyword = words[0]
    if keyword == 'u':
        if len(words) == 3:
            domain = words[1]
            ipa = words[2]
            dns.update(domain, ipa)
        else:
            print("Bad command.")
    elif keyword == 'l':
        if len(words) == 2:
            domain = words[1]
            ipa = dns.lookup(domain)
            print(ipa)
        else:
            print("Bad command.")
    elif keyword == 'q':
        break
    else:
        print("Bad command.")