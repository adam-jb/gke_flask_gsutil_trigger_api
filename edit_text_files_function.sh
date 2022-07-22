edit_and_move_all_files_in_pathway () {

  echo "first input is pathway to input files"
  echo "second input is pathway to output files"

  counter=0
  for item in $(gsutil ls $1)
  do
  	echo $item
	gsutil cp $item temp.csv
	cat temp.csv | sed -e 's:"::g' > temp2.csv
	gsutil cp temp2.csv "$2/output${counter}.csv"
	echo "saved to $2/output${counter}.csv"
	counter=$((counter+1))
  done
}
