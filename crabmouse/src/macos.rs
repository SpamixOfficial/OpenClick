use objc2_core_graphics::CGEvent;
use objc2_core_foundation::CGPoint;

use crate::{MouseFeat, Click, Position};

pub struct Mouse {
    position: Position
}

impl Mouse {
    pub fn new() -> Self {
        let position = Self::get_pos().unwrap();
        Self { position }
    }

    fn get_pos() -> Result<Position, String> {
        let event = match CGEvent::new(None) {
            Some(x) => x,
            None => return Err(format!("Could not get latest event input device"))
        };

        let point: CGPoint = CGEvent::location(Some(&event));
        Ok(Position::new(point.x as usize, point.y as usize))
    }
}

impl MouseFeat for Mouse {
    fn get_position(&self) -> Result<Position, String> {
        Self::get_pos()
    }
}