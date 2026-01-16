from fpdf import FPDF, XPos, YPos
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='letter')

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 200)
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(x1=10, x2=200, y1=21, y2=21)
pdf.output("output.pdf")