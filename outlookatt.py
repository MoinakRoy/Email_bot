import os
import email
attachment_dir=r"C:\Users\USER\Desktop\att"
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))

import imaplib
# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host='imap.outlook.com')
imap_server.login('rmainak01@outlook.com', 'hdud34a01')
imap_server.select()  # Default is `INBOX`

# Find all emails in inbox and print out the raw email data
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, '(RFC822)')

    raw = email.message_from_bytes(msg[0][1])
    get_attachments(raw)