if [ -f submissions.volume ]; then
    echo "submissions.volume already exists"
    exit 1
else
    dd if=/dev/zero of=submissions.volume bs=1024 count=10240
    mkfs.ext4 submissions.volume
fi
mkdir -p submissions
if ! mountpoint submissions; then
    mount -o loop submissions.volume submissions
fi
