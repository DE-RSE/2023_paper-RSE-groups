docker build -t rse_department_survey:latest .
docker stop rse_department_survey 2> /dev/null
umount submissions
docker rm rse_department_survey 2> /dev/null
mount -o loop submissions.volume submissions
docker run -d --restart unless-stopped --name rse_department_survey -p 9000:8014 -v "$(pwd)/submissions:/script/submissions" rse_department_survey:latest
