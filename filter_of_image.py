import cv2


def original(image):
    cv2.imshow("Original image", image)


def black_and_white(image):
    (thresh, blackAndWhiteImage) = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
                                                 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)


def edges_image(image):
    edges = cv2.Canny(cv2.GaussianBlur(image, (5, 5), sigmaX=0), 100, 200)
    cv2.imshow('Edges image', edges)


def gray(image):
    cv2.imshow('gray image', cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


def gaussian_blur(image):
    cv2.imshow('Smooth image', cv2.GaussianBlur(image, (11, 11), sigmaX=0))


image = cv2.resize(cv2.imread("C:\\location_your_image.png"), (200, 200)) # In left, set the image size
original(image)
black_and_white(image)
edges_image(image)
gray(image)
gaussian_blur(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
