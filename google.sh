# bash google.sh facebook.com

#!/usr/bin/bash
domain=$1 
agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36" 
curl -s -A $agent "https://www.google.com/search?q=site%3A*.$domain&start=10" | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+' | grep $domain | sort -u curl -s -A $agent "https://www.google.com/search?q=site%3A*.$domain&start=20" | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+' | grep $domain | sort -u curl -s -A $agent "https://www.google.com/search?q=site%3A*.$domain&start=30" | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+' | grep $domain | sort -u curl -s -A $agent "https://www.google.com/search?q=site%3A*.$domain&start=40" | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+' | grep $domain | sort -u
