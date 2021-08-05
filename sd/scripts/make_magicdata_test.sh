
set -e
magicdata_test_dir=$1
work_path=$2

python scripts/make_magicdata_test.py --init_wav_path $magicdata_test_dir --init_wav_scp_file $work_path/init_wav.scp
