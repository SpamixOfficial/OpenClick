use crate::{MouseFeat, Click, Position};

use windows::Win32::{Foundation::POINT, UI::WindowsAndMessaging::{GetCursorPos, SetCursorPos}};

#[derive(Debug, Clone, Copy)]
pub struct Mouse {
    pub position: Position
}

impl Mouse {
    pub fn new() -> Result<Self, String> {
        let position = match Self::get_pos() {
            Ok(x) => x,
            Err(e) => return Err(e.to_string())
        };
        Ok(Self {
            position
        })
    }

    fn get_pos() -> Result<Position, String> {
        let mut pos: Position = Position::default();
        unsafe {
            let mut raw_pos: POINT = POINT::default();
            match GetCursorPos(&mut raw_pos) {
                Err(e) => return Err(e.to_string()),
                _ => ()
            };
            pos.set(raw_pos.x as usize, raw_pos.y as usize);

        };
        return Ok(pos);
    }
}

impl MouseFeat for Mouse {
}