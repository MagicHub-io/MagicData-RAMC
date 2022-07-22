# MagicData-RAMC Dataset and Baseline

- [Contents](#contents)
    - [Description](#description)
    - [Usage](#usage)
    - [Speaker Diarization Task](#speaker-diarization-task)
    - [ASR Task](#asr-task)
    - [Reference Resource](#reference-resource)
    - [Citation](#citation)
    - [Contact](#contact)
    - [Acknowledgment](#acknowledgment)
    - [Reference](#reference)
    

***
## [Description](#content)

The MagicData-RAMC corpus contains 180 hours of conversational speech data recorded from native speakers of Mandarin Chinese over mobile phones with a sampling rate of 16 kHz. The dialogs in MagicData-RAMC are classified into 15 diversified domains and tagged with topic labels, ranging from science and technology to ordinary life. Accurate transcription and precise speaker voice activity timestamps are manually labeled for each sample. Speakers' detailed information is also provided. As a Mandarin speech dataset designed for dialog scenarios with high quality and rich annotations, MagicData-RAMC enriches the data diversity in the Mandarin speech community and allows extensive research on a series of speech-related tasks, including automatic speech recognition, speaker diarization, topic detection, keyword search, text-to-speech, etc. We also conduct several relevant tasks and provide experimental results to help evaluate the dataset.

***
## [Download](#content)

The dataset can be downloaded on [openslr](http://www.openslr.org/123/).

***
## [Speaker Diarization Task](#content)

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

We formulate CDER (Conversational Diarization Error Rate) to evaluate the performance of the speaker diarization system on the sentence level under conversational scenario. Our [CDER-Metric](https://github.com/MagicHub-io/CDER_Metric) could be used to calculate CDER.

```bash
cd sd/CDER-Metric
python score.py -r ${groundtruth_rttm} -s ${predicted_rttm}
```

***
### Result:


| Method    | DER (collar 0.25) | DER (collar 0) | JER   |  CDER |
| --------- | ----- | ----- | ----- | ----- |
| [VBx](https://github.com/BUTSpeechFIT/VBx) | 5.57 | 17.48 | 45.73 | 26.9 |



***
## [ASR Task](#content)

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
## [Reference Resource](#content)

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
## [Citation](#contents)

If you use MagicData-RAMC dataset in your research, please kindly consider citing our paper:

    @article{yang2022open,
    title={Open Source MagicData-RAMC: A Rich Annotated Mandarin Conversational (RAMC) Speech Dataset},
    author={Yang, Zehui and Chen, Yifan and Luo, Lei and Yang, Runyan and Ye, Lingxuan and Cheng, Gaofeng and Xu, Ji and Jin, Yaohui and Zhang, Qingqing and Zhang, Pengyuan and others},
    journal={arXiv preprint arXiv:2203.16844},
    year={2022}
    }

***
## [Contact](#contents)

If you have any questions, please contact us. You could open an issue on github or [email us](open@magicdatatech.com]). 


***
## [Acknowledgment](#contents)

We thank [@MG623](https://github.com/MG623) for finding label mistakes in CTS-CN-F2F-2019-11-15-1422 ([detail](https://github.com/MagicHub-io/MagicData-RAMC-Challenge/issues/8)). 

***
## [Reference](#contents)

[1] Watanabe, S., Hori, T., Karita, S., Hayashi, T., Nishitoba, J., Unno, Y., Soplin, N.E.Y., Heymann, J., Wiesner, M., Chen, N. and Renduchintala, A., 2018. Espnet: End-to-end speech processing toolkit. arXiv preprint arXiv:1804.00015.

[2] Povey, D., Ghoshal, A., Boulianne, G., Burget, L., Glembek, O., Goel, N., Hannemann, M., Motlicek, P., Qian, Y., Schwarz, P. and Silovsky, J., 2011. The Kaldi speech recognition toolkit. In IEEE 2011 workshop on automatic speech recognition and understanding (No. CONF). IEEE Signal Processing Society.

[3] Gulati, A., Qin, J., Chiu, C.C., Parmar, N., Zhang, Y., Yu, J., Han, W., Wang, S., Zhang, Z., Wu, Y. and Pang, R., 2020. Conformer: Convolution-augmented transformer for speech recognition. arXiv preprint arXiv:2005.08100.

[4] Watanabe, S., Hori, T., Kim, S., Hershey, J.R. and Hayashi, T., 2017. Hybrid CTC/attention architecture for end-to-end speech recognition. IEEE Journal of Selected Topics in Signal Processing, 11(8), pp.1240-1253.

[5] Landini, F., Wang, S., Diez, M., Burget, L., Matějka, P., Žmolíková, K., Mošner, L., Silnova, A., Plchot, O., Novotný, O. and Zeinali, H., 2020, May. But system for the second dihard speech diarization challenge. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 6529-6533). IEEE.

[6] Diez, M., Burget, L., Landini, F. and Černocký, J., 2019. Analysis of speaker diarization based on Bayesian HMM with eigenvoice priors. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 28, pp.355-368.

[7] Ryant, N., Church, K., Cieri, C., Du, J., Ganapathy, S. and Liberman, M., 2020. Third DIHARD challenge evaluation plan. arXiv preprint arXiv:2006.05815.

[8] Watanabe, S., Mandel, M., Barker, J., Vincent, E., Arora, A., Chang, X., Khudanpur, S., Manohar, V., Povey, D., Raj, D. and Snyder, D., 2020. CHiME-6 challenge: Tackling multispeaker speech recognition for unsegmented recordings. arXiv preprint arXiv:2004.09249.

[9] Fu, Y., Cheng, L., Lv, S., Jv, Y., Kong, Y., Chen, Z., Hu, Y., Xie, L., Wu, J., Bu, H. and Xu, X., 2021. AISHELL-4: An Open Source Dataset for Speech Enhancement, Separation, Recognition and Speaker Diarization in Conference Scenario. arXiv preprint arXiv:2104.03603.

