# import re

# fh = open(r"fradulent_emails.txt","r",encoding="utf-8").read()

# for line in re.findall("From:.*", fh):
# 	print(line)

# match = re.findall("From:.*", fh)
# print(type(match))

# Find Name
# for line in match:
# 	print(re.findall("\".*\"",line))

# Find E-Mail
# for line in match:
# 	print(re.findall("\w\S*@.*\w",line))

# for line in match:
# 	print(re.findall("\w\S*@",line))


# for line in match:
# 	print(re.findall("@.*\w",line))

# match = re.search("From:.*", fh)
# print(type(match))
# print(type(match.group()))
# print(match)
# print(match.group())

# address = re.findall("From:.*", fh)
# for item in address:
# 	print(item)
# 	for line in re.findall("\w\S*@.*\w",item):
# 		print(line)
# 		username, domain_name = re.split("@",line)
# 		print("{}, {}".format(username, domain_name))

# sender = re.search("From:.*", fh)
# address = sender.group()
# email = re.sub("From","Email",address)
# print(address)
# print(email)

import re
import pandas as pd
import email

emails=[]

fh = open(r"fradulent_emails.txt","r",encoding="utf8").read()
contents = re.split(r"From r",fh)
# print(contents)
contents.pop(0)
# print(contents)

for item in contents:
	emails_dict = {}
	sender = re.search(r"From:.*", item)
	if sender is not None:
		s_email = re.search(r"\w\S*@.*\w", sender.group())
		s_name = re.search(r":.*<", sender.group())
		print("sender type: "+str(type(sender)))
		print("sender.group() type: "+str(type(sender.group())))
		print("sender: "+str(sender))
		print("sender.group(): "+str(sender.group()))
		print("\n")
	else:
		s_email = None
		s_name = None

	# print(s_email)
	# print(s_name)

	if s_email is not None:
		sender_email = s_email.group()
	else:
		sender_email = None
	emails_dict["sender_email"] = sender_email

	if s_name is not None:
		sender_name = re.sub("\s*<","",re.sub(":\s*","",s_name.group()))
	else:
		sender_name = None
	emails_dict["sender_name"] = sender_name

	# print(sender_email)
	# print(sender_name)

	recipient = re.search(r"To:.*", item)

	if recipient is not None:
		r_email = re.search("\w\S*@.*\w", recipient.group())
		r_name = re.search(":.*<", recipient.group())
	else:
		r_email = None
		r_name = None

	# print(s_email)
	# print(s_name)

	if r_email is not None:
		recipient_email = r_email.group()
	else:
		recipient_email = None

	emails_dict["recipient_email"] = recipient_email

	if r_name is not None:
		recipient_name = re.sub("\s*<","",re.sub(":\s*", "", r_name.group()))
	else:
		recipient_name = None

	emails_dict["recipient_name"] = recipient_name

	date_field = re.search(r"Date:.*", item)

	if date_field is not None:
		date = re.search(r"\d+\s\w+\s\d+", date_field.group())
		print(date_field.group())
		date = re.search(r"\d+\s\w+\s\d+", date_field.group())
		date_star_test = re.search(r"\d*\s\w*\s\d*", date_field.group())
	else:
		date = None

	

	if date is not None:
		date_sent = date.group()
		date_star = date_star_test.group()
	else:
		date_sent = None

	emails_dict["date_sent"] = date_sent

	print(date_sent)
	print(date_star)

	subject_field = re.search(r"Subject: .*", item)

	if subject_field is not None:
		subject = re.sub(r"Subject: ", "", subject_field.group())
	else:
		subject = None

	emails_dict["subject"] = subject

	full_email = email.message_from_string(item)
	body = full_email.get_payload()
	emails_dict["email_body"] = body

	emails.append(emails_dict)

print("Number of emails: " + str(len(emails_dict)))

print("\n")

for key, value in emails[0].items():
	print(str(key) + ": " + str(emails[0][key]))

emails_df = pd.DataFrame(emails)
pd.DataFrame.head(emails_df, n=3)

# emails_df[emails_df["sender_email"].str.contains("maktoob|spinfinder")]

# index = emails_df[emails_df["sender_email"].str.contains(r"\w\S*@maktoob.com")].index.values

# address_Series = emails_df.loc[index]["sender_email"]
# print(address_Series)
# print(type(address_Series))

# address_string = address_Series[0]
# print(address_string)
# print(type(address_string))

# print(emails_df[emails_df["sender_email"]==address_string]["email_body"].values)