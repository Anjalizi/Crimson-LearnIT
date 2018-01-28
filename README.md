# Project for Learn IT, Girl! 3rd Edition
Final implementation of the Learn IT, Girl! project which helps women choose the right makeup products for themselves. :girl::nail_care:

## How to Execute?

```
git clone https://github.com/Anjalizi/Crimson-LearnIT.git 
pip install -r requirements.txt 
python manage.py runserver
```

### The project will run on http://127.0.0.1:8000/ on your preferred browser and implements the following functionalities:

1. Enabling the user to identify her skintone
2. Enabling the user to find out her undertone
3. User uploading her face's image for testing
4. Authorization of the user via SignUp and Login before upload
5. Finding skin color of the user (To be integrated)


## Finding the Skin Color of the User

The skin color of the user can be found out using the K-Means clustering algorithm which displays(here) the 3 most dominant colors in an image, one of which is the skin color
### Execution

```
python color_kmeans.py --image media/pine.jpg --clusters 3 
```
Here,
pine.jpg : Sample image to be evaluated <br>
3 : Number of dominant colors

#### To test the functionality on your own face simply put your face's image in the folder named 'media' and replace 'pine.jpg' by 'path_to_image.jpg'

## Languages, Tools and Frameworks Employed:
Languages I opted for: #### HTML and CSS

* Django - Web framework in Python
* HTML, CSS - Front end foundations
* OpenCV - Library in python used for computer vision
* KMeans Clustering - Machine Learning algorithm for finding dominant colors

## Acknowledgments

* My mentor Irene Nandutu [@Nandutu](https://github.com/Nandutu) for guiding me all through this project, providing me an awesome roadmap and motivating me throughout this four month journey :sparkles:
* Learn IT, Girl! for providing me this great opportunity and learning materials
* Adrian @PyImageSearch for getting me through OpenCV and K-Means Clustering
