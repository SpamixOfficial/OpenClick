use std::{thread, time};

use crabmouse::Position;
use crabmouse::MouseFeat;
#[cfg(all(target_os = "windows", feature = "windows"))]
use crabmouse::windows::Mouse;

#[cfg(all(target_os = "linux", feature = "linux"))]
use crabmouse::linux::Mouse;

#[cfg(all(target_os = "macos", feature = "macos"))]
use crabmouse::macos::Mouse;


fn main() {
    let mouse = Mouse::new();
    let wait = time::Duration::from_secs(2);
    dbg!(mouse.get_position());
    dbg!(mouse.set_position(Position::new(100,100)));
    mouse.test_hold();
    thread::sleep(wait);
    dbg!(mouse.set_relative_position(Position::new(50,0)));
}