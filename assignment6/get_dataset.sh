wget https://huggingface.co/datasets/jianglongye/ece176/resolve/main/CMP_facade_DB_base.zip
wget https://huggingface.co/datasets/jianglongye/ece176/resolve/main/CMP_facade_DB_extended.zip

mkdir dataset

unzip CMP_facade_DB_base.zip -d dataset/

rm dataset/label_names.txt
rm dataset/readme.txt

unzip CMP_facade_DB_extended.zip -d dataset/

rm CMP_facade_DB_base.zip
rm CMP_facade_DB_extended.zip
