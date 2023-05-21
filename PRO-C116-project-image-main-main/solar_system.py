import cv2
image = cv2.imread("solar-system.jpg")
cv2.putText(image,"sun",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"mercury",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"venus",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"earth",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"mars",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"jupiter",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"saturn",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"uranus",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"neptune",(20,300),cv2.FONT_HERSLEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("xyz",image)
cv2.waitKey(0)

##############################! Mam , THE POSITION OF THE TEXTS ARE SAME BECAUSE I CANT'T SEE THE OUTPUT. SO THATS WHY !#################################