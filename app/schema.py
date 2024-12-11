from pydantic import BaseModel, Field


class SandboxTestCSR(BaseModel):
    request_id: int = Field(
        description="We will use this to get the final CSID from ZATCA."
    )
    dispositiobnMessage: str = Field(description="Status message")
    binarySecurityToken: str = Field(
        description="""
        After decoding the in base64, we will get the final CSID.
        later we will extract the signature from this.
        1. Used to create invoice and encryption
        2. Used to login to ZATCA and send invoices
    """
    )
    secret: str = Field(
        description="Used as a password when login to ZATCA to send invoices"
    )
    erros: bool = Field(description="True for error false for successful")
