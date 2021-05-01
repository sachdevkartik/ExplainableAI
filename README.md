<h1 align="center">  Explainable AI using SHAP & CXPlain.  </h1>

## About
  * Machine Learning (ML) based models are often black-box
  * To use ML model in industrial setting it should be fair and reliable
  * Metrics like accuracy-score or r2-score makes it reliable, but one cannot say anything about the fairness of the model
  * ML engineer should be able to explain their models and understand the value and accuracy of their findings
  * In this project, we have tried to interpret a trained ML model using CXPlain and SHAP library


## Project Flow
  * A ML model is trained on a tabular dataset for binary classification task
  * Using this trained model, feature importance for the input features are calculated with the help of CXPlain and SHAP Model interpretation library
 * Results are compared quantitatively.
  * We paste this LaTex code to [Overleaf](https://www.overleaf.com/project) page to see resulting presentation

 
## Requirements
 * cxplain 1.0.3
 * shap 0.37.0
 * tensorflow 2.4.1

## Installation procedure
```python 
pip install cxplain
pip install shap
pip install tensorflow

```  
## Results
 <h3><SHAP>
    <summary>Result 1: Scientists contribution to humanity</summary>

![image](https://user-images.githubusercontent.com/63906053/115167032-90e3a300-a0be-11eb-93f6-4c975537aec0.png)

![image](https://user-images.githubusercontent.com/63906053/115167048-9ccf6500-a0be-11eb-8a7e-b2e36f555949.png)
</details></h3>

 <h3><details >
      <summary> Result 2: Convolutional Neural Network</summary>
  
![image](https://user-images.githubusercontent.com/63906053/115167079-be305100-a0be-11eb-9ee0-8d3ca2ba5f78.png)

![image](https://user-images.githubusercontent.com/63906053/115167084-c5eff580-a0be-11eb-8ef4-89e4d85c17e5.png)
</details></h3>


 <h3><details >
    <summary>Result 3: Industrial Revolution</summary>

![image](https://user-images.githubusercontent.com/63906053/115167425-39463700-a0c0-11eb-98bf-babc00c0b0be.png)

![image](https://user-images.githubusercontent.com/63906053/115167433-44996280-a0c0-11eb-8c6d-5543b344045d.png)

</details></h3>

## Team members
  * [Aditya Pradhan](https://www.linkedin.com/in/aditya-pradhan-3407b69a/)
  * [Kartik Sachdev](https://github.com/sachdevkartik)
  * [Kishore Kunisetty](https://github.com/kishoreKunisetty)
  * [Lennart Mesters](https://www.linkedin.com/in/lennart-mesters-b49873167/)
