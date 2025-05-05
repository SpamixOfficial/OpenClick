/// X11 Specific functionality

use std::fmt::Debug;

use xcb::{x::{QueryPointer, Window}, Connection};

use crate::Position;

pub struct XState {
    root: Window,
    conn: Connection
}

impl Debug for XState {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Debug placeholder") // TODO: Implement nice debug display for window, Connection doesn't have debug so that can be skipped!
    }
}
impl XState {
    pub fn setup() -> Result<Self, String> {
        let (conn, screen_num) = match xcb::Connection::connect(None) {
            Ok(x) => x,
            Err(e) => return Err(e.to_string())
        };

        let setup = conn.get_setup();
        let screen = match setup.roots().nth(screen_num as usize) {
            Some(x) => x,
            None => return Err(format!("Screen number {} wasn't found", screen_num as usize))
        };
        let root = screen.root();

        Ok(Self {
            conn,
            root
        })
    }

    pub fn get_position_absolute(&self) -> Result<Position, String> {
        let cookie = self.conn.send_request(&QueryPointer {window: self.root});
        match self.conn.wait_for_reply(cookie) {
            Err(e) => Err(e.to_string()),
            Ok(x) => Ok(Position(x.root_x() as usize, x.root_y() as usize))
        }
        
    }
}