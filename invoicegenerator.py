import pandas as pd
import glob
import fpdf
from pathlib import Path


# To get the filepath from folders
filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:

    filename=Path(filepath).stem
    invoice_no=filename.split("-")[0]
    invoice_date=filename.split("-")[1]

    pdf = fpdf.FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=10)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=10, txt=f"invoice_no :{invoice_no}", align="L", ln=1)
    pdf.cell(w=0, h=8, txt=f"invoice_Date: {invoice_date}", align="L", ln=1)

    df = pd.read_excel(filepath)

    columns=[item.replace("_"," ").title() for item in df.columns]
    pdf.set_font(family="Times", size=8, style="B")
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=30, h=10, txt=columns[0], align="L", border=1)
    pdf.cell(w=60, h=10, txt=columns[1], align="L", border=1)
    pdf.cell(w=30, h=10, txt=columns[2], align="L", border=1)
    pdf.cell(w=30, h=10, txt=columns[3], align="L", border=1)
    pdf.cell(w=30, h=10, txt=columns[4], align="L", border=1, ln=1)
    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=15, txt=str(row["product_id"]), align="L",border=1)
        pdf.cell(w=60, h=15, txt=str(row["product_name"]), align="L", border=1)
        pdf.cell(w=30, h=15, txt=str(row["amount_purchased"]), align="L", border=1)
        pdf.cell(w=30, h=15, txt=str(row["price_per_unit"]), align="L", border=1)
        pdf.cell(w=30, h=15, txt=str(row["total_price"]), align="L", border=1,ln=1)

    total_sum=df["total_price"].sum()

    pdf.set_font(family="Times", size=10,style="B")
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=30, h=15, txt="", align="L", border=1)
    pdf.cell(w=60, h=15, txt="", align="L", border=1)
    pdf.cell(w=30, h=15, txt="", align="L", border=1)
    pdf.cell(w=30, h=15, txt="", align="L", border=1)
    pdf.cell(w=30, h=15, txt=str(total_sum), align="L", border=1,ln=1)

    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=30, h=15, txt=f"The amount due is: {total_sum} Rupees" , align="L",ln=1)
    pdf.image("invoices/pythonhow.png")



    pdf.output(f"Generatedinvoice/{filename}.pdf")





