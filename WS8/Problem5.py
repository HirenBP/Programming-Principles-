
def book_fever(meetings):
    infected = set()
    results = []

    for meeting in meetings:
        names = meeting.split()
        for i, name in enumerate(names):
            if name.endswith("*"):
                infected.add(name[:-1])
            if name in infected:
                infected.add(names[(i + 1) % len(names)])

        infected_count = len(infected)
        results.append(f"{meeting.count(' ')+1} {' '.join(infected)} {infected_count}")

    return results
source = "//".join(['Data_Files', input('Enter file name: ')])
with open(source, 'r') as f:
    lines = f.readlines()
print(book_fever(lines))