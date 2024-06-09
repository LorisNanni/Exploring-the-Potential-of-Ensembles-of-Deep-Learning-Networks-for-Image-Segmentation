# Exploring the Potential of Ensembles of Deep Learning Networks for Image Segmentation
Exploring the Potential of Ensembles of Deep Learning Networks for Image Segmentation

The link for downloading the code for the ensemble of DeepLabV3+ and the data augmentation code: https://github.com/LorisNanni/An-empirical-study-on-ensemble-of-segmentation-approaches

the links for HardNet and PVT are: https://github.com/james128333/HarDNet-MSEG https://github.com/DengPingFan/Polyp-PVT

the link for HSN is https://github.com/baiboat/HSNet

! very important, you should comment the line (in PVT, HSN and HardNet):

res = (res - res.min()) / (res.max() - res.min() + 1e-8)

otherwise you will always find a foreground region

see line 40 of https://github.com/james128333/HarDNet-MSEG/blob/master/Test.py

see line 40 of https://github.com/DengPingFan/Polyp-PVT/blob/main/Test.py

see line 40 of https://github.com/baiboat/HSNet/blob/main/Test.py

you should comment that normalization also in the training set, e.g. if you use images without foreground pixels.


for extracting the set of images for each test image using HSN and PVT (instead of the single image obtained summing the output of the set of sigmoid function) see test_fus.py In that file: model = HSNet() for using it with PVT you need to recall the PVTmodel.



Note on HSNet and PVT Networks Integration
We have integrated the code provided by the authors for HSNet and PVT networks into our software. However, we have made two significant modifications to the original implementation:

Normalization Adjustment: We have removed the normalization based on the maximum and minimum values. This normalization method was found to be effective only when there is at least one pixel to be segmented in the image. By removing it, we aim to improve the robustness of the segmentation across varying conditions.

Epoch Selection Criterion (check carefully the code you are using): The original implementation selected the optimal number of epochs based on the validation set, which is part of the test set. To prevent data leakage and ensure a fair evaluation, we have revised this approach. The optimal number of epochs is now determined without using the test set, adhering to a more stringent and unbiased validation process.

These changes were made to enhance the reliability and generalizability of our segmentation results. We believe these adjustments provide a more robust framework for practical applications.




Da3.py is the code of Data augmentation 3 of the paper. 
