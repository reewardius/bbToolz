# bash cert.sh facebook.com

target=$1
curl -s "https://crt.sh/?q=%25.$target&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
