import os
import re

def main():
    txt_dir = "/home/chenyifan/Datasets_3/MDT2021S003/TXT"
    wav_dir = "/home/chenyifan/Datasets_3/MDT2021S003/WAV"
    txt_files = os.listdir(txt_dir)
    
    if len(txt_files) != 351:
        raise Exception("Dataset is incomplete. Please check dataset.")
    
    if len(os.listdir(wav_dir)) != 351:
        raise Exception("Dataset is incomplete. Please check dataset.")
    
    patt = '(\d+)-(\d+)-(\d+)-(\d+)'
    for i in range(len(txt_files)-1):
        for x in range(i+1, len(txt_files)):
            j = 1
            while j<5:
                # print(re.match(patt, txt_files[i]))
                lower = re.search(patt, txt_files[i]).group(j)
                # print(lower)
                upper = re.search(patt, txt_files[x]).group(j)
                if int(lower) < int(upper):
                    j = 5
                elif int(lower) == int(upper):
                    j += 1
                else:
                    txt_files[i],txt_files[x] = txt_files[x],txt_files[i]
                    j = 5

    # print(txt_files)

    seg_writter_train = open("segment_train", "w+")
    scp_writter_train = open("wav.scp_train", "w+")
    text_writter_train = open("text_train", "w+")
    rttm_writter_train = open("rttm_gt_train", "w+")
    utt2spk_writter_train = open("utt2spk_train", "w+")

    seg_writter_dev = open("segment_dev", "w+")
    scp_writter_dev = open("wav.scp_dev", "w+")
    text_writter_dev = open("text_dev", "w+")
    rttm_writter_dev = open("rttm_gt_dev", "w+")
    utt2spk_writter_dev = open("utt2spk_dev", "w+")

    seg_writter_test = open("segment_test", "w+")
    scp_writter_test = open("wav.scp_test", "w+")
    text_writter_test = open("text_test", "w+")
    rttm_writter_test = open("rttm_gt_test", "w+")
    utt2spk_writter_test = open("utt2spk_test", "w+")

    for index, txt_file in enumerate(txt_files):
        name = txt_file[:-4]
        wav_name = name + '.wav'
        wav_path = os.path.join(wav_dir, wav_name)
        txt_reader = open(os.path.join(txt_dir, txt_file), )
        txt_all = txt_reader.readlines()

        scp_line = name + ' ' + wav_path + '\n'
        if index < 43:
            scp_writter_test.writelines(scp_line)
        elif index < 332:
            scp_writter_train.writelines(scp_line)
        else:
            scp_writter_dev.writelines(scp_line)

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
            
            if index < 43:
                rttm_writter_test.writelines(rttm_line)
            elif index < 332:
                rttm_writter_train.writelines(rttm_line)
            else:
                rttm_writter_dev.writelines(rttm_line)
               
            if re.match('\[\*\]', text) is not None:
                continue

            start_time_int = start_time.replace('.', '')
            end_time_int = end_time.replace('.', '')
            seg_line = person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + name + ' ' + start_time + ' ' + end_time + '\n'
            text_line =  person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + text + '\n'

            utt2spk_line = person_id + '_' + name + '_' + start_time_int + '_' + end_time_int + ' ' + person_id + '\n'

            if index < 43:
                seg_writter_test.writelines(seg_line)
                text_writter_test.writelines(text_line)
                utt2spk_writter_test.writelines(utt2spk_line)
            elif index < 332:
                seg_writter_train.writelines(seg_line)
                text_writter_train.writelines(text_line)
                utt2spk_writter_train.writelines(utt2spk_line)
            else:
                seg_writter_dev.writelines(seg_line)
                text_writter_dev.writelines(text_line)
                utt2spk_writter_dev.writelines(utt2spk_line)


    return 0

if __name__ == "__main__":
    main()