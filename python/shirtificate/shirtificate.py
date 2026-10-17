# submit50 cs50/problems/2022/python/shirtificate
from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_font("helvetica", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=60, text="CS50 Shirtificate", align="C")

    img_width = 180
    x_coordinate = (210 - img_width) / 2
    pdf.image("shirtificate.png", x = x_coordinate, w=img_width, y=70)

    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255) # Màu trắng
    pdf.set_y(145)
    pdf.cell(w=0, text=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
   main()
