#!/bin/bash
LB=localhost
PORT=2003

while true
do
	MINUTES=`date "+%M"`
	SECONDS=`date "+%S"`
	NOW=`date "+%s"`


	echo -e "test.seconds $SECONDS, test.minutes $MINUTES"
	echo "test.seconds $SECONDS $NOW" | nc $LB $PORT;
	echo "test.minutes $MINUTES $NOW" | nc $LB $PORT;

	echo "travel-content.charlietest2.cpu.cpu0.test 1000 $NOW" | nc $LB $PORT;	

	echo "foo.fuckyou 1000 $NOW" | nc $LB $PORT;	

	sleep 1
done
