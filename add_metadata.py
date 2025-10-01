from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("contract.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# sample metadata from the Google Sheet
metadata = {
    "/Title": "Murabaha Facility Agreement",
    "/ContractStatus": "Draft",
    "/ContractType": "Murabaha",
    "/DateSigned": "10/07/2023",
    "/DocumentOwner": "Legal department",
    "/PartiesInvolved": "ABC Bank",
    "/Jurisdiction": "UAE",
    "/HalalStatus": "halal",
    "/ProfitRate": "5% profit margin",
    "/PaymentTerms": "Deferred payment over 12 months",
    "/ContractAmount": "$500,000",
    "/Notes": "Clause 5: No riba; Clause 8: Delivery terms"}

writer.add_metadata(metadata)

with open("contract_with_metadata.pdf", "wb") as f:
    writer.write(f)

print("Metadata added successfully!")

