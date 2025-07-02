from fpdf import FPDF
import pandas as pd

pdf =FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("pagedetail.csv")


for index, row in df.iterrows():
    t=row["Pages"]
    h=row["Topic"]
    for i in range(t):
        pdf.add_page()
        pdf.set_font(family="Times",style="B",size=12 )
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0,h=12,txt=h, border=0, align="L",ln=1 )
        for i in range(20,298,10):
            pdf.line(10,i,200,i)

        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(254, 0, 0)
        pdf.cell(w=0, h=10, txt=h, border=0, align="R", ln=1)


pdf.output("output.pdf")