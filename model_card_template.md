# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Kaylee Garcia created the model. It is a Random Forest Classifier model using random_state=19 (this random_state is used throughout the entirety of the model). It was made using scikit-learn and categorical features were encoded using OneHotEncoder.

## Intended Use
To predict whether a person's annual salary is above or below $50,000 using demographic and employment information. This was created for use in a Udacity course and is not intended to be used for any real-world decision making. 

## Training Data
The model used 80% of the available data to train with the prediction label set to salary. The categorical features used were: workclass, education, marital-status, occupation, relationship, race, sex, and native-country. These were converted into numeric representations using OneHotEncoding and then the processed features and binary labels were used to fit a random forest classifier. 

## Evaluation Data
The model was tested using the remaining 20% of the data that was not used for training. Performance was evaluated separately for each unique category within the categorical features. Precision, recall, and F1 score were calculated for the overall model as well as each slice.

## Metrics
Precision: 0.7377 (measures how often positive predictions were correct)| Recall: 0.6042 (measures how many actual positive cases were identified) | F1: 0.6643 (balances precision and recall)

## Ethical Considerations
Some demographic categories may have too small of a population in the data to accurately represent some groups. 
This model is for educational purposes only, and should not be used to make any real-world decisions.
Race and sex are sensitive attributes that could cause the model to reproduce historical inequalities in the data.

## Caveats and Recommendations
This model was trained on census data from the United States in 1994 and may not generalize to more recent populations or populations from other countries. Future recommendations include testing the model using newer population data from the United States. If there is a desire to apply to populations of other countries, the model should be trained and tested on data specifically from that country.