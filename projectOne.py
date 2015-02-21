# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# Filename: projectOne.py
#
# Summary: This Program will perform an array of image manipulation that the user decides to 
# choose. Options inculde Image pixalation, applying a grayscale filter, lightening the picture, 
# applying a negation filter,  and shirnking the an image. The user will be able to perform these
# methods to any picture of their liking. 
# 
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

#This function will be called to pixale one sqaure in the image 
#This function will do so by taking in the red, green, and blue vaules
#and taking the average of each and making a new red, green, and blue vaule to 
#be assinged to every pixel in that square.
def pixalate_image(pointA_col, pointA_row, pointB_col, pointB_row, picture, number):
    
    static_square_width = getWidth(picture) / (number)  #Width of square being pixalated
    static_square_height = getHeight(picture) /(number) #Height of square being pixalted 
    												    #total_width are being divided by
    #Initializes the red, green, and blue "buckets" that will hold
    #to sum of all red, greem and blue vaules of every pixel in that
    #square.
    red_bucket = 0
    blue_bucket = 0
    green_bucket = 0
    total_height = getHeight(picture) # Total pixels in the image height
    total_width = getWidth(picture)	 # Total pixels in the image width
    
    average = static_square_width * static_square_height#This is the number that the total red_bucket, green_bucket and blue_bucket
                                                         #will be divided  in order fot the new_blue, new_green and new_blue to be 
                                                         #created as an average number.
    
    
    if pointB_col <= total_width and pointB_row <= total_height:#Checks to see if the square edges don't exceed their bounds 
	# This for loop will go through square and collect its red, green, 
    #and blue vaules, and create an average color for each.
      for x in range(int(pointA_col),int(pointB_col)): 
        for y in range(int(pointA_row), int(pointB_row)):
          pixel = getPixelAt(picture, x, y)
          red_bucket += getRed(pixel)
          blue_bucket += getBlue(pixel)
          green_bucket += getGreen(pixel)
           
         # Creaes average color by dividing the respective "bucket" vaules by the average variable.
          new_red = red_bucket/(average)  
          new_blue = blue_bucket / (average)
          new_green = green_bucket / (average)
          new_color = makeColor(new_red, new_green, new_blue)
      
      # This for loop will go through the same square once again to now replace every pixel with the new colors.
      for x in range(int(pointA_col), int(pointB_col)):
        for y in range(int(pointA_row), int(pointB_row)):
          pixel = getPixel(picture, x, y)
          setColor(pixel, new_color)
      
#This function will be called in the menu if the user selects the option to pixilate the image.        
def selectPicturePixalation(picture):  

  
  number = 120.0 #The number by which the height and width will be divind by to create the dimentions for 
                 #the box that will be pixilated. 
  total_width = getWidth(picture)
  total_height = getHeight(picture)
  
#These variables define the start and end points for the height and width for the sqaure that is being pixalated. 
  pointB_col = total_width / float(number) # Point B of column 
  pointB_row = total_height / float(number) # Point B of row
  pointA_col = 0 
  pointA_row = 0 

  #Amount that is added as x and y positions need to change
  static_square_width = int(getWidth(picture)/ float(number))
  static_square_height =int( getHeight(picture)/ float(number))
  

  
#This nested loop will call the pixilate_image function for every square in the image 
  while pointA_row <= total_height and pointB_row <= total_height:  #This will control the colums being pixilated

    
    while pointA_col <= (total_width):
      pixalate_image(pointA_col, pointA_row, pointB_col, pointB_row ,picture,number)
      pointA_col += static_square_width #changing the point A and B col vaules allows square to shuffle to the right
      pointB_col += int(static_square_width)
      
      show(picture)
      repaint(picture)

      
    #Changing the row vaules, will allow the square to move to the next row down 
    pointA_row += static_square_height
    pointB_row += static_square_height
    
	#Point A and B that were modifed for the column, sets back to orginal coordinates to start pixilateing column from left to right  
    pointA_col = 0
    pointB_col = static_square_width
    
#This function will change the pixels in the image to that of a grayscale    
def grayScalePixel(pixel):
  newRed = getRed(pixel)*0.299
  newGreen = getGreen(pixel)*0.587
  newBlue = getBlue(pixel)* 0.114
  luminance = newRed+newGreen+newBlue
  setColor(pixel, makeColor(luminance,luminance,luminance))
  
#This function will lighten the pixels in the entire image
def lightenPixel(pixel):
  color=getColor(pixel)
  color=makeLighter(color)
  setColor(pixel, color)


#This function will lighten the pixels in the entire image  
def negative(picture):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)

  
#This function will shrink the image to the user's liking  
def shrink(picture, factor):
   width = getWidth(picture)
   height = getHeight(picture)
   image = makeEmptyPicture(width / factor, height / factor)
   
   oldX = 0
   newX = 0
   while oldX < width - factor:
      oldY = 0
      newY = 0
      while oldY < height - factor:
         oldP = getPixel(picture ,oldX, oldY)
         newP = getPixel(image,newX, newY)
         setRed(newP, getRed(oldP))
         setGreen(newP, getGreen(oldP))
         setBlue(newP, getBlue(oldP))
         oldY += factor
         newY += 1
      oldX += factor
      newX += 1
   show(image)
  

#This is where the the images will be manipulated  
def changeImage(option):
  file = pickAFile()
  picture = makePicture(file)
  
  
  if int(option) == 1:
    selectPicturePixalation(picture)
    show(picture)
    repaint(picture)

  elif int(option) == 2:

    for px in getPixels(picture):
      grayScalePixel(px)

  elif int(option) == 3:

    for px in getPixels(picture):
      lightenPixel(px)

  elif int(option) == 4:

      negative(picture)


  elif int(option) == 5:
    factor = requestInteger("Which factor would you like to shrink your image by?")
    shrink(picture, factor)
 
  else:
      showError("Wrong input, please try again.")
  show(picture)
  repaint(picture)

   
     
 
def main():

  
  #Which ever option the user selects from the menu will be stored in the variable option
  option = requestInteger("Please selecet an image manipulation option:\n 1. Pixilate Image \n 2. Grayscale \n 3. Lighten the picture \n 4. Negate picture \n 5. Shirk picture (Original and shrunk will be displayed) \nYou will be prompted to select an image after. \n")
  #After user enters their option, it will take them to the changeImage function

  changeImage(option)
  
  
  
