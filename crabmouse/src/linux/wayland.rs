/// Wayland specific functionality#![allow(non_upper_case_globals)]
use crate::{bindings::uinput::{self, input_event}, Position};

#[derive(Debug, Clone, Copy)]
pub struct WState {
    pos: Position,
    hold: bool
}

impl WState {
    /// Get new WState object
    /// 
    /// All fields will be default on startup because **uinput doesn't have the ability to get current state**.
    /// After use (for example by setting position or by holding) the state will be updated
    pub fn setup() -> Self {
        return Self {pos: Position::default(), hold: bool::default()}
    }

    /// Get current position, **will panic on failure**
    /// 
    /// Alias for get_position_absolute (but uses unwrap)
    pub fn get_position_absolute_unsafe(&self) -> Position {
        self.get_position_absolute().unwrap()
    }

    /// Get current position
    /// 
    /// NOTES: Because of wayland quirks this only fetches the local last-known position 
    /// This means that any eventual mouse movements done by the user will not be present here
    pub fn get_position_absolute(&self) -> Result<Position,String> {
        return Ok(self.pos)
    }

    /// Set **absolute** position to **pos**
    ///
    /// When *relative* is enabled:
    /// > Set position **relative** to last-known position by **pos**
    pub fn set_position(&self, pos: Position, relative: bool) -> Result<(), String> {
        /*input_event event = {
            type_ = 
        };*/
        Ok(());
    }
    
}