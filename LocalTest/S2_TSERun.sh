cd containers/TSEImage
# rm -R output/
# mkdir output
# rm -R input.json
# echo >input.json
# ##### Commented for now, needs to be executed based on output of containers above, and implemented in input.txt
# ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
# xhost + $ip

# docker run --rm -e DISPLAY=$ip:0 --add-host dockerhost:192.168.65.2 -v $(pwd)/output:/output -v $(pwd)/input.json:/input.json datasharing/ttp
###

docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/output:/output \
-v $(pwd)/security_input.json:/security_input.json datasharing/tse