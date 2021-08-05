<!-- # Magic-Data-ASR-SD-Challenge -->

***
## ASR Track

<!-- [MAGICDATA Mandarin Chinese Read Speech Corpus (openslr-68)](http://www.openslr.org/68/)  -->

***
### Data Preparation:


***
### Network Training:

```bash
./run.sh
```

***
### Decoding & Scoring:

```bash
sclite -r ${ref_path} trn -h ${output_path} trn -i rm -o all stdout > ${result_path}
```

***
### Result:

| Method    | Corr  | Sub   | Del   | Ins   | Err   |
| --------- | ----- | ----- | ----- | ----- | ----- |
| [Conformer](https://github.com/espnet/espnet/tree/master/egs2/librispeech/asr1) | 80.1  | 13.7  | 6.3   | 2.8   | 22.8  |


***
### Reference Model:


***
## SD Track

***
### Data Preparation:


***
### Testing:

```bash
./run.sh
```


***
### Result:


| Method    | DER   | JER   |
| --------- | ----- | ----- |
| [VBx](https://github.com/BUTSpeechFIT/VBx) | 7.89  | 47.47 |


***
### Reference Model:


<!-- ***
### xxx:

xx

***
### xxx：

xx

***
### xxx：

xx

>xxx
>
>xxx -->







Dataset:

[VoxCeleb Corpus (openslr-49)](http://www.openslr.org/49/)
[CN-Celeb Corpus (openslr-82)](http://www.openslr.org/82/)

***
## Reference:

[1] Watanabe, S., Hori, T., Karita, S., Hayashi, T., Nishitoba, J., Unno, Y., Soplin, N.E.Y., Heymann, J., Wiesner, M., Chen, N. and Renduchintala, A., 2018. Espnet: End-to-end speech processing toolkit. arXiv preprint arXiv:1804.00015.

[2] Povey, D., Ghoshal, A., Boulianne, G., Burget, L., Glembek, O., Goel, N., Hannemann, M., Motlicek, P., Qian, Y., Schwarz, P. and Silovsky, J., 2011. The Kaldi speech recognition toolkit. In IEEE 2011 workshop on automatic speech recognition and understanding (No. CONF). IEEE Signal Processing Society.

[3] Gulati, A., Qin, J., Chiu, C.C., Parmar, N., Zhang, Y., Yu, J., Han, W., Wang, S., Zhang, Z., Wu, Y. and Pang, R., 2020. Conformer: Convolution-augmented transformer for speech recognition. arXiv preprint arXiv:2005.08100.

[4] Landini, F., Wang, S., Diez, M., Burget, L., Matějka, P., Žmolíková, K., Mošner, L., Silnova, A., Plchot, O., Novotný, O. and Zeinali, H., 2020, May. But system for the second dihard speech diarization challenge. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 6529-6533). IEEE.

[5] Diez, M., Burget, L., Landini, F. and Černocký, J., 2019. Analysis of speaker diarization based on Bayesian HMM with eigenvoice priors. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 28, pp.355-368.

<!-- More details about the Conformer: 

https://arxiv.org/pdf/2005.08100


https://ieeexplore.ieee.org/abstract/document/8910412/

https://arxiv.org/pdf/2002.11356 -->