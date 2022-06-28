# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF, renderPM
# drawing = svg2rlg("./home.svg")
# print(drawing)
# renderPDF.drawToFile(drawing, "file.pdf")


# 2nd
# import cairosvg


# # # Get data from POST
# svg = ("./home.svg")
# print(svg)

# pdf = cairosvg.svg2pdf(bytestring=svg.encode("utf-8"),write_to='image.pdf')
# print(pdf)

# 3rd
# from reportlab.graphics import renderPDF, renderPM
# from svglib.svglib import svg2rlg
# image_path='./home.svg'


# # ex.

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF
# drawing = svg2rlg("./file.svg")
# a=renderPDF.drawToFile(drawing, "file.pdf")
# print(a)


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF
# drawing = svg2rlg("./home.svg")
# a=renderPDF.drawToFile(drawing, "file.pdf")
# print(a)


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF
# drawing = svg2rlg("./home.svg")
# scaleFactor = 1./0.3527
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
# # renderPDF.drawToFile(drawing, "file2.pdf")
# renderPDF.drawToFile(drawing, "file2.pdf", autoSize=0)

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF, renderPM

# drawing = svg2rlg("./home.svg")
# renderPDF.drawToFile(drawing, "file.pdf")
# renderPM.drawToFile(drawing, "file.png", fmt="PNG")


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF

# drawing = svg2rlg('./home.svg')
# renderPDF.drawToFile(drawing, 'ri' +".pdf")


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM
# drawing = svg2rlg("./file.svg")
# renderPM.drawToFile(drawing, "file.png", fmt="PNG")

# def convert_png_to_pdf(image_path, pdf_path):
#     ok = False
#     if not removeAlpha(image_path):
#         print("fail to remove alpha channel")
#         return False
#     try:
#         pdf_bytes = img2pdf.convert(image_path) 
#         file = open(pdf_path, "wb") 
    
#         # writing pdf files with chunks 
#         file.write(pdf_bytes)  
#         file.close()
#         ok = True
#     except:
#         ok = False
#     return ok

# convert_status = convert_png_to_pdf(image_path='E:\\ts.png', pdf_path = 'ts3.pdf')
# if convert_status:
#     print("convert png to pdf successfully!")
# else:
#     print("fail to convert png to pdf!")



# from reportlab.graphics import renderPDF, renderPM
# from svglib.svglib import svg2rlg
# def svg_demo(image_path, output_path):
#     drawing = svg2rlg(image_path)
#     renderPDF.drawToFile(drawing, output_path)
#     renderPM.drawToFile(drawing, 'svg_demo.png', 'PNG')
# if __name__ == '__main__':
#     svg_demo('./file.svg', 'svg_demo.pdf')


import cairosvg
# res = cairosvg.svg2pdf('./filemm.svg')
svg='./home.svg'
pdf = cairosvg.svg2pdf(bytestring=svg.encode("utf-8"))
print(pdf)
