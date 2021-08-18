. path.sh
. cmd.sh

magicdata_test_path=/home/chenyifan/repos/sd-magicdata/wav/ # add your own path
work_dir=./data/magicdata160h_dev_test
sad_dir=$work_dir/sad_part
sad_work_dir=$sad_dir/exp
sad_result_dir=$sad_dir/sad
dia_dir=$work_dir/dia_part
dia_vad_dir=$dia_dir/vad
dia_rttm_dir=$dia_dir/rttm
dia_emb_dir=$dia_dir/embedding
dia_split_rttm_dir=$dia_dir/splited_rttm
dia_stable_rttm_dir=$dia_dir/stable_rttm

stage=4
nj=8


if [ $stage -le 4 ]; then
    # The Speaker Embedding Cluster
    echo "Do the Speaker Embedding Cluster"
    # The meeting data is long so that the cluster is a little bit slow
    scripts/run_cluster.sh $dia_dir
fi

