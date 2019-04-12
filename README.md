# ASVspoof2019

This repository contains materials related to our participation in the ASVspoof 2019 Automatic Speaker Verification Spoofing and Countermeasures Challenge. 

Usually while training deep neural networks we use all the available training data or often tend to add more data points through augmentation techniques. In our work, we propose dataset partitions where we discard lots of data points during training and validation from the original training and development sets. This ensures different attack types are present during training and validation and helps improve system robustness.

Our dataset split protocal files for LA and PA can be found in the respective LA and PA folders. Plesae read the readme file provided inside LA and PA for more details.

## Zero-removal Scripts

We also release our silence removal scripts (both python and matlab) that we used in our work. This is based on a naive approach of counting a consecutive block of zeros as a silence. The scripts are provided inside the scripts folder.

The details of our participation in the ASVspoof 2019 challenge and our post-evaluation intervention experiments on the PA tasks can be found in the following paper (submitted to Interspeech 2019)

https://arxiv.org/abs/1904.04589
