dd if=/dev/zero of=submissions.volume bs=1024 count=10240
mkfs.ext4 submissions.volume
mkdir submissions
