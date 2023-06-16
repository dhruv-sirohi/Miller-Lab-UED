# Novel applications of Generative Adversarial Networks (GANs) in the analysis of ultrafast electron diffraction (UED) images
Applying Machine Learning techniques to solid state physics. 
Currently focused on predicting the ultrafast temperature changes of bismuth molecules, pumped by 800 nm 100 fs laser pulses, through the analysis of the diffraction patterns obtained via ultrafast electron pulses.

<p align="center">
  <img src="https://github.com/dhruv-sirohi/Miller-Lab-UED/blob/main/Project%201:%20Synthetic%20Data%20Classification/Plots%20%2B%20Scans/Bismuth_Diffraction_Pattern.png?raw=true"/>
</p>
 
<div align="center"> Powdered Bismuth's Electron Diffraction Pattern

<div align="left"> 

### Running the Jupyter notebook 

The paper's code can be found in a Jupyter notebook available in the root directory.

Prior to running the notebook, multiple files must be downloaded:
1. The network weights (available here:  https://drive.google.com/drive/folders/1-I5mCXXeSGTpHQVul5g96EmWVlzqXnGF?usp=sharing)
2. The synthetic dataset (available here: https://drive.google.com/drive/folders/1Im-cxjH_oLr3xY7Ow2MuYI0gp7ZzPgqf?usp=sharing)
3. The dataset of lab images (available here: https://drive.google.com/drive/folders/1A4mSKqP-3tkd6p9l9n1eB8jD9b9zQcoa?usp=sharing)

The Jupyter notebook accesses these files using the Google Drive library, so it is advised to save these files to your Google Drive and load them into your Colab instance from there.

Upon changing the default folder paths in the notebook for the datasets and weights to their paths in your instance, the notebook can be run sequentially. Additional documentation can be found in the notebook to explain individual code snippets.
