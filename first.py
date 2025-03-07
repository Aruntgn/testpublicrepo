# To run multiple img's:
img_path = [r"/content/sample_data/img1.jpg", r"/content/sample_data/ocr_img1.jpg"]
ocr = OCR(detect=True)
text_list = ocr.predict(img_path)
for text in text_list:
  print(text)

