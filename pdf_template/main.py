from fpdf import FPDF, XPos, YPos
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='letter')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 200)
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    for y_val in range(20, 260, 10):
        pdf.line(x1=10, x2=200, y1=y_val, y2=y_val)

    pdf.ln(240)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.cell(w=0, h=10, text=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for y_val in range(20, 260, 10):
            pdf.line(x1=10, x2=200, y1=y_val, y2=y_val)

        pdf.ln(250)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.cell(w=0, h=10, text=row["Topic"], align="R")

pdf.output("output.pdf")