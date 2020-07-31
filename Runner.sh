search_dir=$PWD"/inputs"

python -m unittest

echo
echo

for i in "$search_dir"/*
do
    echo "-----Running $i-------"
    echo "-----Output-----"
    python -m geektrust $i
    echo "----Finished----"
    echo
done

echo "All Ran Successfully"