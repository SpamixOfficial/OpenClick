# 🦀Crabmouse🐭

*__What is crabmouse?__*

Crabmouse is a portable and minimal mouse library for rust, specifically created for __OpenClick__ an open source autoclicker!

## Features and targets

If you're writing a cross-platform app it is highly recommended to use the `default` feature. This makes sure that crabmouse will have support for all supported operating systems.

However, if you're writing an application specifically for macos (example) then you most likely only want to enable the `macos` feature instead.

Table of features:

| Feature | Description                  |
| ------- | ---------------------------- |
| default | enables all features         |
| linux   | Enables linux support   |
| windows | Enables windows support |
| macos   | Enables macos support   |

> It should be noted that enabling a feature does not make it compile on your platform; to make windows support compile when using linux you must also configure your target to be windows.

## Wayland

In contrast to X11, wayland does not implement any methods to get the global cursor position - that is the responsibility of each "compositor".
Therefore, without creating a file for every compositor, there's no way to get the cursor position reliably. Sorry about this inconvenience!
