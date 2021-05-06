<h2 align="center">  Explainable AI using SHAP & CXPlain</h2>

## About
  * Machine Learning (ML) based models are often black-box
  * To use ML model in industrial setting it should be fair and reliable
  * Metrics like accuracy-score or r2-score makes it reliable, but one cannot say anything about the fairness of the model
  * ML engineer should be able to explain their models and understand the value and accuracy of their findings
  * In this project, we have tried to interpret a trained ML model using CXPlain and SHAP library
  * This project was developed for a [#hackingforfuture Hackathon](https://websites.fraunhofer.de/hacking-for-future/) organized by [International Center for Networked, Adaptive Production ICNAP](https://www.vernetzte-adaptive-produktion.de/en.html) in coorperation with the [Fraunhofer Project Center at the University of Twente](https://www.utwente.nl/en/fraunhofer/)
   


## Project Flow
  * A ML model is trained on a tabular dataset for binary classification task
  * Using this trained model, feature importance for the input features are calculated with the help of CXPlain and SHAP model interpretation library
 * Results are compared quantitatively.

 
## Requirements
 * cxplain 1.0.3
 * shap 0.37.0
 * pycaret 2.3.0
 * tensorflow 2.4.1
 * plotly 4.14.3 

## Installation procedure
```python 
pip install cxplain
pip install shap
pip install pycaret
pip install tensorflow
pip install plotly
```  
## Results
<details>
      <summary> Light Gradient Boosting Machine Classification Report</summary>
	<br>
 
 ![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/LGB2.png)
</details>

<details>
      <summary> Light Gradient Boosting Machine Confusion Matrix</summary>
	<br>
 
 ![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/LGB1.png)
</details>

<details>
      <summary> Relative importance of features using SHAP</summary>
	<br>
 
 ![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/SHAP1.png)
 ![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/SHAP4.png)
        <br>
#### How a particular feature affects a prediction:

![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/SHAP2.png)

</details>

<details>
      <summary> Relative importance of features using CXPlain</summary>
	<br>
 
 ![alt text](https://github.com/sachdevkartik/ExplainableAI/blob/master/photos/CXplain.png)
</details>

</details></h3>

## Team members
  * [Aditya Pradhan](https://www.linkedin.com/in/aditya-pradhan-3407b69a/)
  * [Kartik Sachdev](https://github.com/sachdevkartik)
  * [Kishore Kunisetty](https://github.com/kishoreKunisetty)
  * [Lennart Mesters](https://www.linkedin.com/in/lennart-mesters-b49873167/)
