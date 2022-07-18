fileExists=10
until [ $fileExists -eq 9 ]
do
  echo "Please enter the name of the file you want to attach: "
  read attachment
  isFile=$(file $attachment | cut -d\ -f2)
  if [[ $isFile = "ASCII" ]]
    then
      fileExists=0
    else
      echo "$attachment is not a text file, please use a different file"
  fi
done
