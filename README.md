# <u>Trip Advisor Hotel Reviews Sentiment Predictions</u>



## Authors

- Janindu Pathirana



## Summary of the Project

This application is based on a sentiment analysis model created using the [Trip Advisor Hotel Reviews](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews)  dataset on [Kaggle](https://www.kaggle.com), and the application is able to predict a rating of 1 - 5 for a given review. Logistic Regression was used to build the prediction model, and the model performed fairly well upon the input of a review. This is my first end to end machine learning project.



#### Key Findings : The model performs really well when predicting the two extreme ends of ratings, which are the ratings of 1 and 5, and its performance drops relatively when predicting the ratings of 2, 3, 4 for a rating based sentiment analysis model.



## Data Source

-  [Trip Advisor Hotel Reviews](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews)



## Tech stack

- Python(All packages used are included in the "requirements.txt" file).



## Method

- Explanatory Data Analysis
- Preprocessing the dataset
- Train Test data split
- Tokenizing the training data 
- Training the model
- Serializing the data object
- Building the web application
- Model Deployment



## Performance results

- Confusion matrix for Logistic Regression Classifier

![CF_logReg](F:\EndToEnd_Projects\Hotel_Reviews\Model_images\CF_logReg.png)

- Precision, Recall, and F1-Score for Logistic Regression Classifier

  |      | Precision | Recall | F1-Score |
  | ---- | :-------- | ------ | -------- |
  | 1    | 0.78      | 0.64   | 0.70     |
  | 2    | 0.46      | 0.43   | 0.44     |
  | 3    | 0.40      | 0.23   | 0.29     |
  | 4    | 0.55      | 0.50   | 0.52     |
  | 5    | 0.70      | 0.84   | 0.77     |

  

- Confusion Matrix for Random Forrest Classifier

  ![CF_RF](F:\EndToEnd_Projects\Hotel_Reviews\Model_images\CF_RF.png)

- Precision, Recall, and F1-Score for Random Forrest Classifier

  |      | Precision | Recall | F1-Score |
  | ---- | :-------- | ------ | -------- |
  | 1    | 0.62      | 0.65   | 0.64     |
  | 2    | 0.36      | 0.24   | 0.29     |
  | 3    | 0.35      | 0.23   | 0.28     |
  | 4    | 0.47      | 0.40   | 0.43     |
  | 5    | 0.63      | 0.78   | 0.70     |



- **Final model used for the project : Logistic Regression**

- **Reason for using Logistic Regression**:

  In a multi-class sentiment analysis problem the main objective is to identify what that sentiment actually is for the provided data, or simply to classify the data. Therefore Logistic Regression is a very good algorithm since it classifies the data distinctly according to the relationships.

  Furthermore, the recall score and F1- score was used to make a decision between Logistic Regression and Random Forrest Classifier. The recall score gives an understanding about how much of the predictions were correct for all the data in a given class, therefore in this type of a problem recall score plays a much important role than the precision score.



## Lessons learned from the project

- The model is more accurate in predicting the extreme ends of ratings which are 1 and 5 and is less accurate when the rest if the rating. This behaviour understandable since the ratings of 2, 3, and 4 are very subjective, and even a human might struggle to identify which is which.

- ![](F:\EndToEnd_Projects\Hotel_Reviews\Model_images\Count of reveiws for each Rating.png)

  The above image shows that there is a definite data imbalance for the ratings of 1, 2, and 3 when compared with the rest of the ratings. Therefore having more data which represent the ratings of 1, 2, and 3 would have definitely increased the overall performance of the model.

- Additionally, fitting Random forrest classifier models takes time and the pickle files can get very large due to the tress, branches and leaves of the classifier. It Literally and figuratively becomes a forrest.

