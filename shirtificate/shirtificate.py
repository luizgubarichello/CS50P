from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C",new_x = 120, new_y = 150)

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", x = 10, y = 60, w = 190)
pdf.set_font("Times", size=12)
pdf.cell(0, 0, "I TOOK CS50", align = "C")
pdf.output("new-tuto3.pdf")