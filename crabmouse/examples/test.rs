#[cfg(all(target_os = "windows", feature = "windows"))]
use crabmouse::windows::Mouse;

#[cfg(all(target_os = "linux", feature = "linux"))]
use crabmouse::linux::Mouse;

#[cfg(all(target_os = "macos", feature = "macos"))]
use crabmouse::macos::Mouse;


fn main() {
    dbg!(Mouse::new());
}