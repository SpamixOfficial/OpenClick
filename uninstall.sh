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


##  check if its actually not null, otherwise we will get new bumble bee
# Added just in case the name wont be a constant anymore in the future

pkgname="openclick"


if [[ -n $pkgname ]]; then
    sudo rm /usr/bin/openclick
    sudo rm -r "/usr/share/licenses/$pkgname"
    sudo rm -r "/usr/share/doc/$pkgname"
    sudo rm -r "/etc/$pkgname"
    echo "Removal Success!"

else
    echo "Package name is null. Cannot proceed with removal."
fi

exit 0