#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X "POST" "$1" -sd "email:hr@holbertonschool & subject: I will always be here for PLD"
