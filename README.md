# nginx-ultimate-bad-bot-blocker-duplicate-ip-remover

This is a Python script solves the problem that after installing https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker, Nginx logs are filled with 

```
[warn] 28495#28495: duplicate network "138.199.57.151", value: "O", old value: "1" in /etc/nginx/conf.d/globalblacklist.conf:18898
[warn] 28495#28495: duplicate network '143.244.38.129", value: "O", old value: "1" in /etc/nginx/conf.d/globalblacklist.conf:18914
[warn] 28495#28495: duplicate network "195.181.163.194", value: "O", old value: "1" in /etc/nginx/conf.d/globalblacklist.conf:19009
[warn] 28495#28495: duplicate network "5.188.120. 15", value: "O", old value: "1" in /etc/nginx/conf.d/globalblacklist.conf:19136
[warn] 28495#28495: duplicate network "89.187.173.66", value: "O", old value: "1" in /etc/nginx/conf.d/globalblacklist.conf:19183
```

## Instructions

Put `weedOutDuplicateIPs.py` in the same directory as `update-ngxblocker` script. 
Open `update-ngxblocker` script and find the line overwrites globalblacklist.conf with the new version and invoke the weedOutDuplicateIPs.py script after that. It should look like this:
```
       case "$retval" in
             0) print_message "$dl_msg...${BOLDGREEN}[OK]${RESET}\n\n"
                mv $tmp $output
                /usr/bin/python /usr/local/sbin/weedOutDuplicateIPs.py
                ;;
            22) printf "$dl_msg...${BOLDRED}ERROR 404: $url${RESET}\n\n";;
            28) printf "$dl_msg...${BOLDRED}ERROR TIMEOUT: $url${RESET}\n\n";;
             *) printf "$dl_msg...${BOLDRED}ERROR CURL: ($retval){RESET}\n\n";;
        esac
```

Then run `update-ngxblocker` script to test if it works.

Related issue: https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/issues/548.


