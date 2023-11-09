filename = input("Enter the file name:")
senderz = {}
with open(filename, 'r') as file:
    for line in filename:
        if line.startswith("From"):
            text = line.split()
            email = text[1]
            sender = email.split(".")[0]
            senderz[sender] = senderz.get(sender,0) + 1
            print(senderz)
most_count = 0
most_sender = None
for sender, count in senderz.items():
    if count > most_count:
        most_sender = sender
        most_count = count
print(most_sender,"sent",most_count,"emails")
