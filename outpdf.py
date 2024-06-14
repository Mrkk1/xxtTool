import os
import pdfkit

# 确保wkhtmltopdf在系统的PATH中
# pdfkit.config(wkhtmltopdf='/path/to/wkhtmltopdf')

def convert_md_to_pdf(md_file):
    try:
        # 获取PDF文件的路径
        pdf_filename = md_file.replace('.md', '.pdf')
        # 使用pdfkit转换Markdown文件为PDF文件
        pdfkit.from_file([md_file], pdf_filename)
        print(f"Converted {md_file} to {pdf_filename}")
    except Exception as e:
        print(f"Failed to convert {md_file} to PDF: {e}")

def convert_all_md_to_pdf(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            md_path = os.path.join(directory, filename)
            convert_md_to_pdf(md_path)

# 调用函数，转换当前目录下所有的.md文件
convert_all_md_to_pdf('.')