use objc2_core_foundation::CGPoint;
use objc2_core_graphics::{CGEvent, CGEventTapLocation, CGEventType, CGMouseButton};

use crate::{Click, MouseFeat, Position};

#[cfg(target_os = "macos")]
impl Click {
    fn into_cg_mouse_event(self, down: bool) -> CGEventType {
        match self {
            Self::Left => {
                if down {
                    CGEventType::LeftMouseDown
                } else {
                    CGEventType::LeftMouseUp
                }
            }
            Self::Right => {
                if down {
                    CGEventType::RightMouseDown
                } else {
                    CGEventType::RightMouseUp
                }
            }
            Self::Middle => {
                if down {
                    CGEventType::OtherMouseDown
                } else {
                    CGEventType::OtherMouseUp
                }
            }
        }
    }

    fn into_cg_mouse_button(self) -> CGMouseButton {
        match self {
            Self::Left => CGMouseButton::Left,
            Self::Middle => CGMouseButton::Center,
            Self::Right => CGMouseButton::Right,
        }
    }
}

pub struct Mouse {
    //position: Position, // currently useless since we need to fetch cursor position for every action
}

impl Mouse {
    pub fn new() -> Self {
        //let position = Self::get_pos();
        Self {} //position }
    }

    fn get_pos() -> Position {
        let event = CGEvent::new(None);

        let point: CGPoint = CGEvent::location(event.as_deref());
        Position::from(point)
    }

    fn set_pos(pos: Position) {
        let event = CGEvent::new_mouse_event(
            None,
            CGEventType::MouseMoved,
            pos.into(),
            CGMouseButton::Left,
        );

        CGEvent::post(CGEventTapLocation::HIDEventTap, event.as_deref());
    }

    fn post_mouse_click(down: bool, btn: Click) {
        let pos = Self::get_pos();
        let mouse_button = btn.clone().into_cg_mouse_button();
        let event = CGEvent::new_mouse_event(
            None,
            btn.into_cg_mouse_event(down),
            pos.into(),
            mouse_button,
        );

        CGEvent::post(CGEventTapLocation::HIDEventTap, event.as_deref());
    }
}

impl MouseFeat for Mouse {
    fn get_position(&self) -> Result<Position, String> {
        Ok(Self::get_pos())
    }

    fn set_position(&self, pos: Position) -> Result<(), String> {
        Self::set_pos(pos);
        Ok(())
    }

    fn set_relative_position(&self, pos: Position) -> Result<(), String> {
        let current_pos = Self::get_pos();
        Self::set_pos(current_pos + pos);
        Ok(())
    }

    fn click_grab(&self, click: Click) -> Result<(), String> {
        Self::post_mouse_click(true, click);
        Ok(())
    }

    fn click_release(&self, click: Click) -> Result<(), String> {
        Self::post_mouse_click(false, click);
        Ok(())
    }

    fn click(&self, click: Click) -> Result<(), String> {
        Self::click_grab(&self, click)?;
        Self::click_release(&self, click)
    }
}
