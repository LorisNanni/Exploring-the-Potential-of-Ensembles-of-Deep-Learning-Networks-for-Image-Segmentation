# Exploring-the-Potential-of-Ensembles-of-Deep-Learning-Networks-for-Image-Segmentation
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
