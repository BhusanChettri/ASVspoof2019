Per speaker utterances in Bonafide class - DEV set
second column shows the number of utterances

LA_0069 154
LA_0070 140
LA_0071 140
LA_0072 154
LA_0073 140
LA_0074 154
LA_0075 154
LA_0076 140
LA_0077 154
LA_0078 154
LA_0099 77
LA_0100 77
LA_0101 77
LA_0102 126
LA_0103 126
LA_0104 126
LA_0105 77
LA_0106 126
LA_0107 126
LA_0108 126

Total files = 2548

Note that from the above 20 speakers, 
the first 10 speakers (0069 to 0078) appears in
both bonafide and spoofed classes. However, the other
10 speakers (0099 to 108) are only present in
bonafide class.

================================================
Per speaker utterances in Spoof class - DEV

LA_0069 2484
LA_0070 1848
LA_0071 1848
LA_0072 2484
LA_0073 1848
LA_0074 2484
LA_0075 2484
LA_0076 1848
LA_0077 2484
LA_0078 2484

Total files = 22296

** Each of these 10 speakers appear in all 6 spoofing attack conditions. The speaker
audio files are distributed uniformly across all attacks. These numbers are shown below 

LA_0069 414
LA_0070 308
LA_0071 308
LA_0072 414
LA_0073 308
LA_0074 414
LA_0075 414
LA_0076 308
LA_0077 414
LA_0078 414

#######################################################################################
Splitting the original Dev set into 2 parts: one for Earlystopping and other for Logistic
regression training (fusion weights)

attacks_for_training=                     ['SS_2', 'SS_4', 'US_1', 'VC_4']
attacks_for_modelSelection=               ['SS_1','VC_1']
attacks_for_LR=                           ['SS_2', 'SS_4', 'US_1', 'VC_4', 'SS_1','VC_1'] #keep all attacks in DEV

[a] Early stopping (ES) list
   i) Bonafide Class 
      * Out of 20 speakers, we use 12 speakers (8 female and 4 male). 
      * The speakers Ids are: 
        ['LA_0102','LA_0103','LA_0104','LA_0107','LA_0108','LA_0100','LA_0105','LA_0069','LA_0070','LA_0072','LA_0073', 'LA_0074','LA_0076','LA_0077'] 

      * This gives 1820 bonafide files

   ii)Spoof Class
      * We consider two attacks for ES: SS_1 and VC_1. We did not include these attacks during training.
      * Out of 20 speakers available in Bonafide class, only 10 speakers are seen in Spoof class as described earlier.
      * From these 10 speakers, we use only 6 speakers for Spoof class in Early stopping (4 female and 2 male)
      * The speaker Ids are: ['LA_0069','LA_0070','LA_0072','LA_0074','LA_0076','LA_0077']

      * This gives us 5160 spoof files - corresponding to above speakers and two spoofing attack condition

   ** Therefore, total no. of files in this list (for early stopping) is 6980

[b] Logistic Regression (weight fusion) list
   i) Bonafide class: 
     * We use those 8 speakers (4 male and 4 female) that we did not use in ES in [a] i)
     * The speakers ids are: 
     ['LA_0099','LA_0101','LA_0106','LA_0071','LA_0075','LA_0078']
     * This give us 728 bonafide files
     
   ii) Spoof class:
     * We consider all 6 attack condition ['SS_1','SS_2', 'SS_4', 'US_1', 'VC_1', 'VC_4']
     * We use those 4 speakers (1 male and 2 female) that we did not use in [a] ii).
     * The speakers are
     ['LA_0071','LA_0075','LA_0078'] 
     * This gives us 6816 spoof utterances.

   ** Therefore, the total no. of files in the LR list is 7554

** However, we have thrown a large amount of data in order to make list as unique as possible.


Query:
1) Training Logistic Regression fusion using Bosaris toolkit with following data partition
   728 genuine examples and 6816 spoofed examples. Does the toolkit handle such a biased 
   data to learn optimal weights? Need to clarify this asap !!




Split Summary:

Train:
From the original training protocal file we discard all spoof files belonging to attack condition 'SS_1' and 'VC_1'.
Thus our training set has only 4 attack conditions out of the original 6 conditions from ASVspoof2019.LA.cm.train.trn protocal file.
The file ASVspoof2019.LA.cm.train_split.trn.txt contains the list of files we used for training all our models in the LA tasks.




Dev: 
We split the original dev protocal file ASVspoof2019.LA.cm.dev.trl.txt into two parts. First one we use for model selection (early stopping etc)
and the other for training the logistic regression (LR) fusion weights. For better generalizability, we use only those two attack conditions that 
we discarded during training in our early stopping/validation list. This means we use only spoof files belonging to the two attack conditions 'SS_1' and 'VC_1' 
for selecting our model parameters. This applies to all our deep and shallow models under the LA tasks. For logistic regression sub-protocal we keep all
the 6 attack conditions but speakers (both bonafide and spoof) used in early stopping are not included in the logistic regression sub-protocal list.
Though we are discarding a lot of data points during training and validation but we hope that our approach of data selection helps better generalizability
on the unseen test examples. The two dev protocal files are named as as ASVspoof2019.LA.cm.dev_split_earlystop.trl.txt and ASVspoof2019.LA.cm.dev_split_LR.trl
respectively. We make our used protocal files publicly available online. footnote: github. For further details please read the readme.txt file in the 
github link provided.








