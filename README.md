# Miller-Lab-UED
Applying Machine Learning techniques to solid state physics. More specifically, classifying molecules by the diffraction patterns made by ultrafast electron pulses.

<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Bismuth_Diffraction_Pattern.png?raw=true"/>
</p>
 
<div align="center"> Electron Diffraction Pattern for Bismuth Powder

<div align="left"> 
  
### Project 1: Synthetic Data Classification

  Diffraction data is generated using CrystalMaker 9 (http://crystalmaker.com/) by varying atomic displacements parameters such as Uiso. It is labeled by the value of the parameter which is being varied.
  
  This data is used to train a CNN for a regression (if there is a large number of labels) or image classification (if there are relatively fewer labels).
  
  The performance of transfer learning approaches (convolutional layers pretrained on ImageNet are used) is also determined
  
### To Do:
  Provide background on diffraction + Bragg's Law

