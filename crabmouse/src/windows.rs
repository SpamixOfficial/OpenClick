use crate::{Click, MouseFeat, Position};

use windows::Win32::{
    Foundation::{GetLastError, POINT},
    UI::{
        Input::KeyboardAndMouse::{
            SendInput, INPUT, INPUT_0, INPUT_MOUSE, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP,
            MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_RIGHTDOWN,
            MOUSEEVENTF_RIGHTUP, MOUSEINPUT,
        },
        WindowsAndMessaging::{GetCursorPos, SetCursorPos},
    },
};

use std::mem;

#[derive(Debug, Clone, Copy)]
pub struct Mouse {
    //pub position: Position,
}

impl Mouse {
    pub fn new() -> Self {
        //let position = Self::get_pos().unwrap();
        Self { }//position }
    }

    fn get_pos() -> Result<Position, String> {
        let mut pos: Position = Position::default();
        unsafe {
            let mut raw_pos: POINT = POINT::default();
            match GetCursorPos(&mut raw_pos) {
                Err(e) => return Err(e.to_string()),
                _ => (),
            };
            pos.set(raw_pos.x as usize, raw_pos.y as usize);
        };
        return Ok(pos);
    }

    fn set_pos(pos: Position) -> Result<(), String> {
        unsafe {
            match SetCursorPos(pos.0 as i32, pos.1 as i32) {
                Err(e) => Err(e.to_string()),
                _ => Ok(()),
            }
        }
    }
    /// TODO: Not working atm, pls fix!!
    /// Windows has dedicated left-right-middle up and down codes, so sadly i can't make a "works for all" solution here
    fn send_mouse(click: Click, down: bool) -> Result<(), String> {
        unsafe {
            let event = if down {
                match click {
                    Click::Left => MOUSEEVENTF_LEFTDOWN,
                    Click::Right => MOUSEEVENTF_RIGHTDOWN,
                    Click::Middle => MOUSEEVENTF_MIDDLEDOWN,
                }
            } else {
                match click {
                    Click::Left => MOUSEEVENTF_LEFTUP,
                    Click::Right => MOUSEEVENTF_RIGHTUP,
                    Click::Middle => MOUSEEVENTF_MIDDLEUP,
                }
            };
            let mut raw_inarr: Vec<INPUT> = vec![];
            raw_inarr.push(INPUT {
                r#type: INPUT_MOUSE,
                Anonymous: INPUT_0 {
                    mi: MOUSEINPUT {
                        dwFlags: event,
                        mouseData: 0,
                        dx: 0,
                        dy: 0,
                        dwExtraInfo: 0,
                        time: 0,
                    },
                },
            });
            let sent_events = SendInput(&raw_inarr, mem::size_of::<INPUT>() as i32);
            if sent_events != (raw_inarr.len() as u32) {
                let errcode = GetLastError().0;
                Err(format!(
                    "WinAPI only sent {sent_events} out of {} events | Error: {errcode}",
                    raw_inarr.len() as i32,
                ))
            } else {
                Ok(())
            }
        }
    }
}

impl MouseFeat for Mouse {
    fn get_position(&self) -> Result<Position, String> {
        Self::get_pos()
    }

    fn set_position(&self, pos: Position) -> Result<(), String> {
        Self::set_pos(pos)
    }
    fn set_relative_position(&self, pos: Position) -> Result<(), String> {
        let relative_pos = Self::get_pos()?;
        Self::set_pos(relative_pos + pos)
    }

    fn click(&self, click: Click) -> Result<(), String> {
        Self::send_mouse(click, true)?;
        Self::send_mouse(click, false)
    }

    fn click_grab(&self, click: Click) -> Result<(), String> {
        Self::send_mouse(click, true)
    }

    fn click_release(&self, click: Click) -> Result<(), String> {
        Self::send_mouse(click, false)
    }
}
