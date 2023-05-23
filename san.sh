# bash san.sh facebook.com

domain=$1
sed -ne 's/^\( *\)Subject:/\1/p;/X509v3 Subject Alternative Name/{N;s/^.*\n//;:a;s/^\( *\)\(.*\), /\1\2\n\1/;ta;p;q; }' < <(openssl x509 -noout -text -in <(openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' \-connect $domain:443 ) ) | grep -Po '((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+'
