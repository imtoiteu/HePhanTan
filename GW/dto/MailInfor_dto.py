from pydantic import BaseModel

class MailInfo(BaseModel):
    from_: str = "MTA Shop <mtashop@gmail.com>"
    to: str
    subject: str
    body: str
    attachments: str = None
