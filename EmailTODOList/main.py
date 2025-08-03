import smtplib, ssl
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import TrelloConnector

config = configparser.ConfigParser()
config.read("config.ini")

sender_email = config["EMAIL"]["sender_email"]
receiver_email = config["EMAIL"]["receiver_email"]
password = config["EMAIL"]["password"]
port = 465  # For SSL

current_date = datetime.datetime.now().date()
subject = f"To-Do List {current_date}"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

trello_api_key = config["TRELLO"]["public"]
trello_token = config["TRELLO"]["token"]
trello_list_id = config["TRELLO"]["main_board_to_do_list_id"]
trello = TrelloConnector.Trello(trello_api_key, trello_token)

cards = trello.get_card_names_from_list(trello_list_id)
to_do_list = '\n'.join(cards)

to_do_list_message_part = MIMEText(to_do_list, "plain")

message.attach(to_do_list_message_part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())