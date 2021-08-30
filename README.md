# Magic Data ASR-SD Challenge

***
## 规则说明：

(1) 数据：训练数据只允许使用提供的 160h 对话数据集，以及 [MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/), [VoxCeleb Data (openslr-49)](http://www.openslr.org/49/), [CN-Celeb Corpus (openslr-82)](http://www.openslr.org/82/)。允许使用公开的噪声数据集 (如 [MUSAN (openslr-17)](https://openslr.org/17/), [RIRNoise (openslr-28)](https://openslr.org/28/)) 进行数据增广，但需要注明来源。禁止使用其他来源的数据(包括无监督数据)训练出的预训练模型。

(2) 方法：方法不限，允许包括模型融合，预训练-finetune，无监督自适应在内的所有方法，但需要符合 (1) 中的数据使用规范。

(3) 测试：测试数据与 160h 对话数据同源。ASR 赛道的测试集会给出时间点标注信息。测试集中不会出现训练集中存在的 [*] 等非语言符。 

(4) 打分：ASR 赛道标点符号，非语言符不参与最终 WER 计算。

***
## RULES EXPLANATION:

(1) DATA: Only provided 160h dialog dataset, [MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/), [VoxCeleb Data (openslr-49)](http://www.openslr.org/49/) and [CN-Celeb Corpus (openslr-82)](http://www.openslr.org/82/) are allowed. Data augmentation could be used to process the training sets, and only public noise datasets (such as [MUSAN (openslr-17)](https://openslr.org/17/), [RIRNoise (openslr-28)](https://openslr.org/28/)) are allowed. Pre-train model using other datasets (including unlabeled data) are not allowed in this challenge.

(2) METHOD: There are no limit on method in the challenge. Such as model combination, pre-training and finetune, unsupervised adaptation are all allowed. Note that all methods should follow the rule (1).

(3) TESTING: The testing data is homologous to the 160h dialog dataset. And timestamps of testing data will be provided on ASR track. Nonlinguistic symbols such as [*] will not appear in testing set.

(4) SCORING: On ASR track, punctuation marks and nonlinguistic symbols will not involve in WER calculation.

***
## ASR Track

<!-- [MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/)  -->

For ASR track, we use [Conformer](https://github.com/espnet/espnet/tree/master/egs2/librispeech/asr1) implemented by [Espnet](https://github.com/espnet/espnet) to conduct speech recognition. 160h development set is devided into two part: 140h audio recordings are merged with [MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/) for training, while the other 20h audio recordings are reserved for testing.

***
### Data Preparation:

Run prepare_magicdata_160h.py and prepare_magicdata_750h.py under scripys folder.

***
### Network Training:

```bash
./run.sh
```

***
### Decoding & Scoring:

For scoring, sclite of [Espnet](https://github.com/espnet/espnet) could be used to obtain WER.   

```bash
sclite -r ${ref_path} trn -h ${output_path} trn -i rm -o all stdout > ${result_path}
```

***
### Result:

| Method    | Corr  | Sub   | Del   | Ins   | Err   |
| --------- | ----- | ----- | ----- | ----- | ----- |
| [Conformer](https://github.com/espnet/espnet/tree/master/egs2/librispeech/asr1) | 80.1  | 13.7  | 6.3   | 2.8   | 22.8  |


***
## SD Track

For speaker diarization track, we use [VBHMM x-vectors (aka VBx)](https://github.com/BUTSpeechFIT/VBx) trained by [VoxCeleb Data (openslr-49)](http://www.openslr.org/49/) and [CN-Celeb Corpus (openslr-82)](http://www.openslr.org/82/) on this task. X-vectors embeddings are extracted by [ResNet](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf), and besides, agglomerative hierarchical clustering with variational Bayes HMM resegmentation are conducted to get final result.

***
### Data Preparation:

Run prepare_magicdata_160h.py under scripys folder.

***
### Testing & Scoring:

```bash
./run.sh
```

For scoring, [DIHARD Socring Tools](https://github.com/nryant/dscore) could be used to calculate DER, JER and so on. We already add this repo as a git submodule under our project.

```bash
git submodule update --init --recursive
cd sd/dscore
python score.py --collar 0.25 -r ${groundtruth_rttm} -s ${predicted_rttm}
```

***
### Result:


| Method    | DER   | JER   |
| --------- | ----- | ----- |
| [VBx](https://github.com/BUTSpeechFIT/VBx) | 7.89  | 47.47 |


***
## Reference Resource

### Open Source project:

[Kaldi](https://github.com/kaldi-asr/kaldi) [Espnet](https://github.com/espnet/espnet) [VBx](https://github.com/BUTSpeechFIT/VBx) [DIHARD Socring Tools](https://github.com/nryant/dscore)



### Dataset:

[MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/)

[VoxCeleb Data (openslr-49)](http://www.openslr.org/49/)

[CN-Celeb Corpus (openslr-82)](http://www.openslr.org/82/)


***
### Model:

[Baidu Cloud Drive](https://pan.baidu.com/s/1RMM4R8-b0-t6AZuuJ6opIQ)  (Password: utwh)


***
## Reference Paper

[1] Watanabe, S., Hori, T., Karita, S., Hayashi, T., Nishitoba, J., Unno, Y., Soplin, N.E.Y., Heymann, J., Wiesner, M., Chen, N. and Renduchintala, A., 2018. Espnet: End-to-end speech processing toolkit. arXiv preprint arXiv:1804.00015.

[2] Povey, D., Ghoshal, A., Boulianne, G., Burget, L., Glembek, O., Goel, N., Hannemann, M., Motlicek, P., Qian, Y., Schwarz, P. and Silovsky, J., 2011. The Kaldi speech recognition toolkit. In IEEE 2011 workshop on automatic speech recognition and understanding (No. CONF). IEEE Signal Processing Society.

[3] Gulati, A., Qin, J., Chiu, C.C., Parmar, N., Zhang, Y., Yu, J., Han, W., Wang, S., Zhang, Z., Wu, Y. and Pang, R., 2020. Conformer: Convolution-augmented transformer for speech recognition. arXiv preprint arXiv:2005.08100.

[4] Watanabe, S., Hori, T., Kim, S., Hershey, J.R. and Hayashi, T., 2017. Hybrid CTC/attention architecture for end-to-end speech recognition. IEEE Journal of Selected Topics in Signal Processing, 11(8), pp.1240-1253.

[5] Landini, F., Wang, S., Diez, M., Burget, L., Matějka, P., Žmolíková, K., Mošner, L., Silnova, A., Plchot, O., Novotný, O. and Zeinali, H., 2020, May. But system for the second dihard speech diarization challenge. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 6529-6533). IEEE.

[6] Diez, M., Burget, L., Landini, F. and Černocký, J., 2019. Analysis of speaker diarization based on Bayesian HMM with eigenvoice priors. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 28, pp.355-368.

[7] Ryant, N., Church, K., Cieri, C., Du, J., Ganapathy, S. and Liberman, M., 2020. Third DIHARD challenge evaluation plan. arXiv preprint arXiv:2006.05815.

[8] Watanabe, S., Mandel, M., Barker, J., Vincent, E., Arora, A., Chang, X., Khudanpur, S., Manohar, V., Povey, D., Raj, D. and Snyder, D., 2020. CHiME-6 challenge: Tackling multispeaker speech recognition for unsegmented recordings. arXiv preprint arXiv:2004.09249.

[9] Fu, Y., Cheng, L., Lv, S., Jv, Y., Kong, Y., Chen, Z., Hu, Y., Xie, L., Wu, J., Bu, H. and Xu, X., 2021. AISHELL-4: An Open Source Dataset for Speech Enhancement, Separation, Recognition and Speaker Diarization in Conference Scenario. arXiv preprint arXiv:2104.03603.

<!-- More details about the Conformer: 

https://arxiv.org/pdf/2005.08100


https://ieeexplore.ieee.org/abstract/document/8910412/

https://arxiv.org/pdf/2002.11356 -->