mod x11;
use std::env;
use x11::XState;
use crate::{MouseFeat, Click, Position};

#[derive(Debug, PartialEq, PartialOrd,)]
enum DisplaySession {
    Wayland,
    X11
}

#[derive(Debug)]
pub struct Mouse {
    disp: DisplaySession,
    position: Position,
    xstate: Option<XState>
}

impl Mouse {
    pub fn new() -> Self {
        let disp = match env::var_os("WAYLAND_DISPLAY") {
            Some(_) => DisplaySession::Wayland,
            None => DisplaySession::X11
        };
        let mut position = Position::default();
        let mut xstate = None;
        
        // X11 init, wayland has separate!
        if disp == DisplaySession::X11 {
            xstate = Some(XState::setup().expect("Wasn't able to initialize XState on X11 session..."));
            position = xstate.as_ref().unwrap().get_position_absolute().expect("XState was able to initialize but absolute pointer location wasn't available");
        }
        return Mouse { disp, position, xstate }
    }
}

impl MouseFeat for Mouse {
}