# UED-Net
Applying Machine Learning techniques to solid state physics. 
Currently focused on classifying molecules by the diffraction patterns made by ultrafast electron pulses.

<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Bismuth_Diffraction_Pattern.png?raw=true"/>
</p>
 
<div align="center"> Powdered Bismuth's Electron Diffraction Pattern

<div align="left"> 
  
### Project 1: Synthetic Data Classification

  Diffraction data was generated using CrystalMaker 9 (http://crystalmaker.com/) by varying atomic displacements parameters such as uiso. The data was labeled by uiso value. The generated dataset was relatively tiny, only made up of 165 diffraction patterns, which posed a challenge for generability.
  
This data was used to train a CNN to classify the diffraction patterns. After 65 epochs, the network attained a validation accuracy of ~94%.

  
<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Accuracy_Plot.png"/>
</p>
 
<div align="center"> Test Accuracy over Training

<div align="left"> 

<br />
  
This neural net was then applied to data collected in the lab. Because of uiso's relationship with temperature, it should increase over the course of a scan. Ideally, the network would detect this and would show a gradual increase in uiso as a scan progresses. While this is seen in _some_ cases, this is not always the case.
  
<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/02_21_scan_12.png"/>
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/02_21_scan_14.png"/> 
</p> 

<div align="center"> 
  Predicted uiso values for scan #12 (left) and scan #14 (right). <br /> The trend of the predicted values on the left resembles the expected trend in uiso values
<div align="left"> 

  
### To Do:
  Provide an introduction to diffraction + Bragg's Law

