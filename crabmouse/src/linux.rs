use std::env;

use crate::{MouseFeat, Click, Position};

enum DisplaySession {
    Wayland,
    X11
}

pub struct Mouse {
    disp: DisplaySession,
    position: Position
}

impl Mouse {
    /*pub fn new() -> Self {
        let disp = match env::var_os("WAYLAND_DISPLAY") {
            Some(_) => DisplaySession::Wayland,
            None => DisplaySession::X11
        };
    }*/
}

impl MouseFeat for Mouse {
}