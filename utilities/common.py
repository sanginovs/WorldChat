import time
import boto3
from flask import current_app

def utc_timestamp():
    '''this is a helper function which returns time'''
    return int(time.time())
    
def email(to_email, subject, body_html, body_text):
    if current_app.config.get("TESTING") or not current_app.config.('AWS_SEND_MAIL'):
        return False
    client = boto3.client('ses')
    return client.send_email(
        Source='shersanginov6505@gmail.com',
            Destination={
                'ToAddresses': [
                    to_email,
                ]
            },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                },                
            }
        }
    )