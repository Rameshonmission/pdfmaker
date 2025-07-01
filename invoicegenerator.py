import pandas as pd
import glob
import fpdf
from pathlib import Path
import datetime

filepaths = glob.glob("invoices/*.xlsx")
invoicedate= datetime.datetime.now()
formatted_invoice_date=invoicedate.strftime("%Y-%m-%d %H:%M:%S")
for filepath in filepaths:
    df=pd.read_excel(filepath)
    filename=Path(filepath).stem
    invoice_no=filename.split("-")[0]
    pdf = fpdf.FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=10)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=10, txt=f"invoice_no :{invoice_no}", align="L", ln=1)
    pdf.cell(w=0, h=8, txt=f"invoice_Date: {formatted_invoice_date}", align="L", ln=1)

    for index,row in df.iterrows():
        for item in row:
            pdf.cell(w=0,h=5,txt=str(item),border=1,ln=0)
            pdf.ln(5)

    pdf.output(f"Generatedinvoice/{filename}.pdf")





