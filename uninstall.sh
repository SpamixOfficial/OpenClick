#!/usr/bin/bash
set -e

if [[ "$EUID" != 0 ]]; then
    echo "Sudo was not enabled."

    sudo -k
    if sudo true; then
        echo "Correct password, running uninstallation."
    else
        echo "Wrong Password, exiting."
        exit 1
    fi
fi
pkgname="openclick"

sudo rm /usr/bin/openclick
sudo rm -r "/usr/share/licenses/$pkgname"
sudo rm -r "/usr/share/doc/$pkgname"
sudo rm -r "/etc/$pkgname"

echo "Successfully removed!"
exit 0