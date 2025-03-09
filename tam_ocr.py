# Import the OCR tamil package
!pip install ocr_tamil
from ocr_tamil.ocr import OCR


# Initiating the OCR model based on 
ocr = OCR(detect=True)

#  Smart card (vertical position)
img_path = r"/content/sample_data/img_smcrd_vert.jpg"
texts = ocr.predict(img_path)
print(texts[0])
# ['', 'வதுதளம்', 'நுகர்வோர்பாது', 'மனைமானாஸ்', '/FAMILYCARD', 'சிவப்பிரகாசம்', 'கோவிந்தசாயி', 'எண்ணைஅ7', 'மெயின்ரோடு', 'நகர்', 'மாடம்பாக்கம்தாம்பரம்', 'களைனான்', 'அரசு', '15/05/1979', 'பிளாட்', 'புவனேஸ்வரி', 'சென்னை', 'வழங்கல்மற்றும்', 'குடும்பத்தலைவுரின்பெயர்', 'மமைது', 'அட்டை', 'பெயர்', 'தந்தைகணவரின்', 'உணவுப்பொருள்', 'குடும்ப', 'பிறந்த', 'தேதி', 'முகவரி', 'NPHH-S', '333473348290']

# Smart card (normal position)
img_path = r"/content/sample_data/img_smcrd.jpg"
texts = ocr.predict(img_path)
print(texts[0])

# To run multiple img's:
img_path = [r"/content/sample_data/img1.jpg", r"/content/sample_data/ocr_img1.jpg"]
ocr = OCR(detect=True)
text_list = ocr.predict(img_path)
for text in text_list:
  print(text)


'''  ############

# Import the OCR tamil package

# !pip install ocr_tamil

from ocr_tamil.ocr import OCR
ocr = OCR(detect=True)

'''
#  Smart card (vertical position)
img_path = r"/content/sample_data/img_smcrd_vert.jpg"
texts = ocr.predict(img_path)
print(texts[0])
# arun: ['', 'வதுதளம்', 'நுகர்வோர்பாது', 'மனைமானாஸ்', '/FAMILYCARD', 'சிவப்பிரகாசம்', 'கோவிந்தசாயி', 'எண்ணைஅ7', 'மெயின்ரோடு', 'நகர்', 'மாடம்பாக்கம்தாம்பரம்', 'களைனான்', 'அரசு', '15/05/1979', 'பிளாட்', 'புவனேஸ்வரி', 'சென்னை', 'வழங்கல்மற்றும்', 'குடும்பத்தலைவுரின்பெயர்', 'மமைது', 'அட்டை', 'பெயர்', 'தந்தைகணவரின்', 'உணவுப்பொருள்', 'குடும்ப', 'பிறந்த', 'தேதி', 'முகவரி', 'NPHH-S', '333473348290']
# siva: ['', 'வதுதளம்', 'நுகர்வோர்பாது', 'மனைமானாஸ்', '/FAMILYCARD', 'சிவப்பிரகாசம்', 'கோவிந்தசாயி', 'எண்ணைஅ7', 'மெயின்ரோடு', 'நகர்', 'மாடம்பாக்கம்தாம்பரம்', 'களைனான்', 'அரசு', '15/05/1979', 'பிளாட்', 'புவனேஸ்வரி', 'சென்னை', 'வழங்கல்மற்றும்', 'குடும்பத்தலைவுரின்பெயர்', 'மமைது', 'அட்டை', 'பெயர்', 'தந்தைகணவரின்', 'உணவுப்பொருள்', 'குடும்ப', 'பிறந்த', 'தேதி', 'முகவரி', 'NPHH-S', '333473348290']
'''

# Smart card (normal position)
img_path = r"/content/sample_data/img_smcrd.jpg"
texts = ocr.predict(img_path)
print(texts[0])

'''
arun: 
siva: ['உணவுப்பொருள்', 'தமிழ்நாடு', 'அரசு', 'வழங்கல்', 'மற்றும்', 'நுகர்வோர்', 'பாதுகாப்புத்துரை', 'GOVERNMENT', 'OF', 'TAMILNADU', 'CIVIL', 'SUPPLIES', 'AND', 'CONSUMER', 'PROTECTION', 'DEPARTMENT', 'குடும்ப', 'அட்', 'டை', '/', 'FAMILY', 'CARD', 'குடும்பத்', 'தலைவரின்', 'பெயர்:', 'சிவப்பிரகாசம்', 'கோ', 'தந்தை', 'கணவரின்', 'பெயர்', 'கோவிந்தசாமி', 'பிறந்த', 'தேதி', '15/05/1979', 'முகவரி', 'பிளாட்', 'என்', 'புக்கு', '2', 'வது', 'தளம்', 'கவது', 'மெயின்', 'ரோடு', 'புவ்னேஸ்வரி', 'நகர்', 'NPHH-S', 'மாடம்பாக்கம்தாம்பரம்', 'தென்', '333473348290', 'சென்னை', 'கிருப்பத']
'''
'''  ############

# hi
