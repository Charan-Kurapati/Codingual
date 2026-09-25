import cv2
image = cv2.imread('example.jpg')
grey_image = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
resized_image = cv2.resize(grey_image,(224,224))
cv2.imshow('Processed Image',resized_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('Greyscale_resized_image',resized_image)
    print("Image Saved As Greyscale_resized_image.jpg...")
else:
    print("Image not Saved...")

cv2.destroyAllWindows()
print("Proccessed Image Dimensions",resized_image.shape)