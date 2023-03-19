from ArabicOcr import arabicocr
from numba import jit, cuda
import cv2

#@jit(target_backend='cuda')
#def xx():
#image_path = 'test.jpg'
#print(image_path[-3: len(image_path)])
'''out_image = 'out.jpg'
results = arabicocr.arabic_ocr(image_path, out_image)
print(results)
words = []
for i in range(len(results)):
	word = results[i][1]
	words.append(word)
#with open('file.txt', 'w', encoding='utf-8') as myfile:
	#myfile.write(str(words))



import cv2
img = cv2.imread('out.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img)
'''
'''from pdf2image import convert_from_path

poppler_path = r'C:\Program Files\poppler-0.68.0\bin'
pdf_path = "C:\\Users\\lamay\\Downloads\\اختبار إسلامية ثاني متوسط الفصل الدراسي الاول.pdf"

images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
print(images)
for count, img in enumerate(images):
    img_name = f"page_{count}.png"
    img.save(img_name, "PNG")
t = 'templates\\'
for i in range(t):
    print(f'{t}//')'''
