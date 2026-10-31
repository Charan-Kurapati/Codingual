import cv2
image = cv2.imread("example.jpg")

if image is None:
    print("ERROR:Image not found!...")
    print("Please check that example.jpg si in your working directory...")

else:   
    print("Image loaded successfully!")

    small_image = cv2.resize(image,(200,200))

    medium_image = cv2.resize(image,(400,400))

    large_image = cv2.resize(image,(600,600))

    cv2.imshow("small_image-200 x 200",small_image)
    cv2.imshow("medium_image-400 x 400",medium_image)
    cv2.imshow("large_image-600 x 600",large_image)

    cv2.imwrite("example_small.jpg",small_image)
    cv2.imwrite("example_medium.jpg",medium_image)
    cv2.imwrite("example_large.jpg",large_image)

    print("All resized images have been saved successfully!")
    print("Press any key to close all image windows,")

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    print("Program completed successfully!")