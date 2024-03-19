#!/usr/bin/bash
set -e

if [[ "$EUID" != 0 ]]; then
    echo "Sudo was not enabled."

    sudo -k
    if sudo true; then
        echo "Correct password, running installation."
    else
        echo "Wrong Password, exiting."
        exit 1
    fi
fi


pkgname="openclick"

python install.py || python3 install.py || echo 'Python is not installed, exiting...'

if [[ -n $pkgname ]]; then

sudo install -Dm755 linux/cli.py /usr/bin/openclick
sudo install -Dm444 LICENSE "/usr/share/licenses/$pkgname/LICENSE"
sudo install -Dm444 README.md "/usr/share/doc/$pkgname/README.md"
sudo install -Dm666 settings.json "/etc/$pkgname/settings.json"

echo "Install Success!"
fi

else echo "Package name is null. Exiting"

exit 0