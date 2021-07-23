# Miller-Lab-UED
Applying Machine Learning techniques to solid state physics. More specifically, classifying molecules by the diffraction patterns made by ultrafast electron pulses.

<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Bismuth_Diffraction_Pattern.png?raw=true"/>
</p>
 
<div align="center"> Powdered Bismuth's Electron Diffraction Pattern

<div align="left"> 
  
### Project 1: Synthetic Data Classification

  Diffraction data was generated using CrystalMaker 9 (http://crystalmaker.com/) by varying atomic displacements parameters such as Uiso. The data was labeled by the value of the varied parameter. The generated dataset was relatively tiny, only made up of 165 diffraction patterns, which posed a challenge for generability.
  
  This data was used to train a CNN to classify the diffraction patterns. After 65 epochs, the network attained a validation accuracy of ~92%.

  
<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Accuracy_Plot.png"/>
</p>
 
<div align="center"> Test Accuracy over Training

<div align="left"> 
  


  
### To Do:
  Provide an introduction to diffraction + Bragg's Law

