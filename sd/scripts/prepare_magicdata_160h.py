import os
import re

def main():
    txt_dir = "/home/chenyifan/Datasets_3/Magicdata_160h/TXT"
    txt_files = os.listdir(txt_dir)

    wav_dir = "/home/chenyifan/Datasets_3/Magicdata_160h/WAV"

    seg_writter_train = open("segment_train", "a+")
    scp_writter_train = open("wav.scp_train", "a+")
    text_writter_train = open("text_train", "a+")
    rttm_writter_train = open("rttm_gt_train", "a+")
    utt2spk_writter_train = open("utt2spk_train", "a+")

    seg_writter_test = open("segment_test", "a+")
    scp_writter_test = open("wav.scp_test", "a+")
    text_writter_test = open("text_test", "a+")
    rttm_writter_test = open("rttm_gt_test", "a+")
    utt2spk_writter_test = open("utt2spk_test", "a+")

    for txt_file in txt_files:
        name = txt_file[:-4]
        number = int(name[-4:])
        wav_name = name + '.wav'
        wav_path = os.path.join(wav_dir, wav_name)
        txt_reader = open(os.path.join(txt_dir, txt_file), )
        txt_all = txt_reader.readlines()

        scp_line = name + ' ' + wav_path + '\n'
        if number < 1420:
            scp_writter_train.writelines(scp_line)
        else:
            scp_writter_test.writelines(scp_line)


        for line in txt_all:
            splited_str = line.split("\t", 4)
            time = splited_str[0][1:-1]
            time_str = time.split(",")
            start_time = time_str[0]
            end_time = time_str[1]
            during_time = str(round(float(end_time) - float(start_time), 2))
            person_id = splited_str[1]
            text = splited_str[3][:-1]

            rttm_line = 'SPEAKER ' + name + ' 1 ' + start_time + ' ' + during_time + ' <NA> <NA> ' + person_id + ' <NA> <NA>\n'

            if number < 1420:
                rttm_writter_train.writelines(rttm_line)
            else:
                rttm_writter_test.writelines(rttm_line)
            if re.match('\[\*\]', text) is not None:
                continue

            start_time_int = start_time.replace('.', '')
            end_time_int = end_time.replace('.', '')
            seg_line = person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + name + ' ' + start_time + ' ' + end_time + '\n'
            text_line =  person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + text + '\n'

            utt2spk_line = person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + person_id + '\n'

            # train set
            if number < 1420:
                seg_writter_train.writelines(seg_line)
                text_writter_train.writelines(text_line)
                utt2spk_writter_train.writelines(utt2spk_line)
            # test set
            else:
                seg_writter_test.writelines(seg_line)
                text_writter_test.writelines(text_line)
                utt2spk_writter_test.writelines(utt2spk_line)





    return 0

if __name__ == "__main__":
    main()