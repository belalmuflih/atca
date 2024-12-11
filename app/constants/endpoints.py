from pydantic import ConfigDict, Field, BaseModel


class URLs(BaseModel):
    model_config = ConfigDict()
    sandbox_compliance: str = Field(
        default="https://gw-fatoora.zatca.gov.sa/e-invoicing/developer-portal/compliance",
        description="""
        This is a compliance CSID (CCSID) that is issued by the einvoicing system as it is a prerequisite to complete the compliance steps.
        The CCSID is sent in the authentication certificate header in the compliance api calls.
        
        The CSR specification required to perform the Compliance API call is covered in section 4.3 of the Developer Portal user manual.
        
        source: https://sandbox.zatca.gov.sa/IntegrationSandbox
        """,
    )
    sandbox_invoices: str = Field(
        "https://gw-fatoora.zatca.gov.sa/e-invoicing/developer-portal/compliance/invoices",
        description="""
        It performs compliance checks on einvoice documents such as:
            - Standard invoice.

            - Standard debit note.

            - Standard credit note.

            - Simplified Invoice.

            - Simplified credit note.

            - Simplified debit note.
        """,
    )
    sandbox_clear_single_invoice: str = Field(
        "https://gw-fatoora.zatca.gov.sa/e-invoicing/developer-portal/invoices/reporting/single",
        description="""
        Reports a single SIMPLIFIED invoice, credit note, or debit note. 
        Specifically, it accepts simplified invoice, credit note, or debit note
        encoded in base64 and validates it to ensure:

        Compliance to the UBL2 XSD.

        EN 16931 Rules set.

        KSA Specific Rules set.

        KSA Rules set will override EN 16931 Rules set in case the same rule exists in both sets. 
        QR Code validation

        Cryptographical Stamp validation

        Previous Invoice Hash Validation (PIH)
        """,
    )


URLs = URLs()
