from fpdf import FPDF
import pandas as pd

pdf =FPDF(orientation="P", unit="mm",format="A4")

df = pd.read_csv("pagedetail.csv")
for index in df.iterrows():

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=12 )
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], border=1, align="L",ln=1 )
    pdf.line(10,22,200,22)



pdf.output("output.pdf")