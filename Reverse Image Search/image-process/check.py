import numpy
import PIL
from PIL import Image
import urllib.request
from numpy import asarray
import pandas as pd
from pandas import DataFrame
import statistics

# reading from excel file
data = pd.read_excel(r'C:\Users\Vedansh\Desktop\selectedimages.xlsx') 
url_list = []
url_list = data['IMAGE_URL']

standarddeviations = []
meanOfImage = []
#iterating over every image
for i in range (0,len(url_list)):
    urllib.request.urlretrieve( url_list[i],"img.png") #retrieval
    

    an_image = PIL.Image.open("img.png")
    image_sequence = an_image.getdata()
    image_array = numpy.array(image_sequence)

   
    image_vector = []
    for j in range(0, len(image_array)):   #iterating over every prixel                                        
        mean_color = (image_array[j][0] + image_array[j][1] + image_array[j][2])/3 #(R+G+B)/3
        image_vector.append(mean_color)



    standard_deviation = round(statistics.pstdev(image_vector), 3)
    mean = round(statistics.mean(image_vector), 3)

    print("Standard Devation: " + str(standard_deviation) + " and Mean: " + str(mean))

    meanOfImage.append(mean)
    standarddeviations.append(standard_deviation)

exp = pd.DataFrame()
exp['IMAGE URL'] = url_list[0:len(url_list)]
exp['Standard Devation'] = standarddeviations[0:len(url_list)]
exp['Mean'] = meanOfImage[0:len(url_list)]

exp.to_excel('result_images.xlsx', index=False)
    


    





