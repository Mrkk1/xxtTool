import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from PyPDF2.generic import NameObject

def add_watermark(input_pdf, output_pdf, watermark_text):
    # 创建 PDF 读取器和写入器
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 设置水印的大小
    c = canvas.Canvas("temp_watermark.pdf", pagesize=letter)
    c.setFont("Helvetica", 36)
    c.setFillAlpha(0.5)
    c.rotate(30)
    c.drawString(350, 400, watermark_text)
    c.drawString(350, 250, 'NOT FOR SELL')
    
    c.drawString(350, 50, watermark_text)
    
    c.save()

    watermark = PdfReader("temp_watermark.pdf")

    # 遍历所有页面并添加水印
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        page.merge_page(watermark.pages[0])
        writer.add_page(page)

    # 保存结果到输出文件
    with open(output_pdf, 'wb') as f:
        writer.write(f)

    # 删除临时水印文件
    os.remove("temp_watermark.pdf")

def main():
    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        if file_name.endswith(".pdf"):
            input_pdf = os.path.join(current_directory, file_name)
            output_pdf = os.path.join(current_directory, f"{os.path.splitext(file_name)[0]}_水印版.pdf")
            add_watermark(input_pdf, output_pdf, "592631053")

if __name__ == "__main__":
    main()
