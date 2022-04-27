# mle_assesment

Assessment for Fetch Rewards MLE Apprentiship

Challenge: Given image size (y,x) and list of corner tuples [(x1,y1), ...,(x4,y4)], return image of y*x evenly spaced pixel coordinates

How to run:
1. clone repository into local machine

2. navigate to mle_assessment directory

3. build docker image using command:
docker build -t mle_assesment .

4. run image using command:
docker run -d -p 5000:5000 mle_assement

5. navigate to http://localhost:5000/ in your web browser

6. input (y, x) image size and list of 4 corner tuples into degsignated boxes and press run.

7. output will be displayed on page. 


Files:
- app.py: file that runs app

- controller.py: class used to handle user input

- model.py: class used to store user input

- pixel_util.py: file containing methods used to handle corners and generate image

- requirements.txt: list of requirements used for application

- Dockerfile: file used to containerize flask app

- testing.py: file used to unit test pixel_util.py
