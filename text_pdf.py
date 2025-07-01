
from pathlib import Path
import fpdf
import glob

filepaths= glob.glob("Textcontent/*.txt")


for filepath in filepaths:
    print(filepath)
    filename=Path(filepath).stem
    with open(filepath,"r") as file:
        content=file.read()

    header=filename.upper()

    pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",size=15,style="B")
    pdf.set_text_color(0,0,254)
    pdf.cell(w=0,h=15,txt=header,align="C",ln=1)
    pdf.set_font(family="Times", size=10, style="I")
    pdf.set_text_color(254, 0, 0)
    pdf.multi_cell(w=0, h=10, txt=content)

    pdf.output(f"converted_text/{filename}.pdf")
