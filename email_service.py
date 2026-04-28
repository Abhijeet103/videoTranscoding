import boto3

ses =  boto3.client('ses')



sender="abhijeet179346@gmail.com"

def send_email():
    recipients=["xyz@gmail.com"]

    subject = "Upload confirmation"
    email_text = "file upload successful"

    body = f"""
    <html>
        <body>
        <h1>{email_text}</h1
        </body>
    </html>
    """

    response = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': recipients,
        } ,
        Message={
            "Subject": {
                "Data": subject ,
            } ,
            'Body': {
                'Text': {"Data":email_text},
                'Html': {'Data':body},
            }
        }
    )

    print("email sent !")