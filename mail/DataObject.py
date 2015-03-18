class mailMeta:
    Sender = ''
    Recipient = []
    Timestamp = 0
    Subject = ''
    SenderIP = ''
    SenderHostName = ''
    Mail = ''
    MailId = ''

    def __init__(self, row):
        self.Sender = row["Sender"]
        self.Recipient = row['Recipient(s)']
        self.Timestamp = row['Timestamp']
        self.Subject = row['Subject']
        self.SenderIP = row['SenderIP']
        self.SenderHostName = row['SenderHostName']
        self.Mail = row['Mail']
        self.MailId = self.parsemainid(self.Mail)


    def parsemainid(self, normalId):
        array = normalId.split(".")
        return array[-2].split("\\")[-1]