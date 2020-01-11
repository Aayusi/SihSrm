# Sentiment Analysis from Text Feedback

This is the official code repository for 'TotallyNotBots'. This ML backed sentiment analysis platform on customer reviews on Amazon products was developed during SIH SRM AP Internal Hackathon.

### TotallyNotBots

* Aayusi Biswas
* Tuhin Sarkar
* Vatsal Rathod
* Sarvesh Shroff
* Naveen Edala
* Khushboo Maheshwari

### Overview

#### Problem Satement: NM396-ISRO
##### Sentiment Analysis from text feedback: 
Webportals like Bhuvan get vast amount of feedback from the users. To go through all the feedbacks can be a tedious job. Develop software to categorize opinions expressed in feedback forums. This can be utilized for feedback management system. The software must provide the classification of individual comments/reviews.

##### Dataset:
The Multi-Domain Sentiment Dataset contains product reviews taken from Amazon.com from many product types (domains).

##### Solution:
A web based software that classifies reviews in real time as either a 'Positive' or a 'Negative' review of the product.

* Data Collection
The data file is provided as a JSON file from the website itself. Since *Bhuvan* is a software service, we chose reviews for Amazon Android apps. The data contains approximately 750,000 data points and has the following data columns:

1. reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
2. asin - ID of the product, e.g. 0000013714
3. reviewerName - name of the reviewer
4. helpful - helpfulness rating of the review, e.g. 2/3
5. reviewText - text of the review
6. overall - rating of the product
7. summary - summary of the review
8. unixReviewTime - time of the review (unix time)
9. reviewTime - time of the review (raw)

* Data Preparation
We load the dataset onto a pandas dataset through a JSON parser. Then, the reviews are characterized as either positive or negative based on the rating and a column named 'Sentiment' is added, this will act as the target for training later. We then clean the text by removing stop words and any unnecessary uppercasing or symbols. This data is now ready for training.

* Model Training
The text is vectorized through the TfdifVectorizer module after being pipelined with the help of Pipeline module. After than an extensive GridSearch model is trained and the model then is pickled to a file named 'model.pkl'. On testing the data on around 100,000 data points, an accuracy of 94% is achieved. 

* Prediction over live-feed
The webapp takes in reviews and results if it is a positive or a negative feedback.

#### Technology used

Backend Dependencies:
* Python
* NLTK
* Scikit-learn
* Numpy/Pandas
* Python Pickle

Frontend Dependancies:
* Flask
* HTML/CSS

Domains:
* Artificial Intelligence [Natural Language Processing]
* Real-time package handling
* Webapp development

#### Screenshots/Demo Video

![Nice](/images/SA.png)

[Have a look at the Youtube video](https://youtu.be/v8Lo2EIrgHc)

#### Usage

1. Clone the repository
```git clone https://github.com/Aayusi/SihSrm```  

2. Open folder 'webapps'
```cd webapps```
```pip install requirements.txt```

3. [Download 'model'](https://drive.google.com/uc?id=1DFx7JbfGkn61dUlGMG04lnTYl_iMCZhi&export=download)

4. Run the application
```flask run```
