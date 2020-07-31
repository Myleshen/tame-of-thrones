search_dir="$PWD/inputs"

python -m unittest $PWD/tests/test_CommandLineParser.py
python -m unittest $PWD/tests/test_FileParser.py
python -m unittest $PWD/tests/test_Solver.py

rm  "$PWD/actual_output/"*
let index=1
echo
echo "=====Program Output======"
for i in "$search_dir"/*
do
    filename=$(basename "$i")
    read -d'-' -a filenamearray <<< "$filename"
    touch "$PWD/actual_output/${filenamearray}-output${index}.txt"
    savefile="$PWD/actual_output/${filenamearray}-output${index}.txt"
    let index=$index+1
    python -m geektrust $i | tee $savefile 
done
echo "==========END============"

echo
echo

echo "Running Test To Check if the given input is correct"
python -m unittest $PWD/tests/test_IntegrationTest.py

echo "All Ran Successfully"