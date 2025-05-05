pub mod x11;
use crate::{Click, Position,MouseFeat};
use std::env;
use x11::XState;

#[derive(Debug, PartialEq, PartialOrd)]
enum DisplaySession {
    Wayland(XState),
    X11(XState),
}

#[derive(Debug)]
pub struct Mouse {
    disp: DisplaySession,
    position: Position,
}

impl Mouse {
    pub fn new() -> Self {
        let disp = match env::var_os("WAYLAND_DISPLAY") {
            Some(_) => DisplaySession::Wayland(XState::setup()), //TODO: Wayland bs
            None => DisplaySession::X11(XState::setup()),
        };
        let position = match &disp {
            DisplaySession::X11(state) => state.get_position_absolute_unsafe(),
            DisplaySession::Wayland(state) => state.get_position_absolute_unsafe(),
        };

        return Mouse { disp, position };
    }
}

impl MouseFeat for Mouse {
    fn get_position(&self) -> Result<Position, String> {
        match &self.disp {
            DisplaySession::X11(state) => state.get_position_absolute(),
            DisplaySession::Wayland(state) => state.get_position_absolute(),
        }
    }

    fn set_position(&self, pos: Position) -> Result<(), String> {
        match &self.disp {
            DisplaySession::X11(state) => state.set_position(pos, false),
            DisplaySession::Wayland(state) => state.set_position(pos, false),
        }
    }

    fn set_relative_position(&self, pos: Position) -> Result<(), String> {
        match &self.disp {
            DisplaySession::X11(state) => state.set_position(pos, true),
            DisplaySession::Wayland(state) => state.set_position(pos, true)
        }
    }
}
