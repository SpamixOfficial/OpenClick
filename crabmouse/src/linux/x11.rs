/// X11 Specific functionality
use std::{cmp::Ordering, fmt::Debug};

use xcb::{
    x::{ButtonIndex, Cursor, EventMask, GrabButton, ModMask, QueryPointer, WarpPointer, Window},
    Connection, Xid,
};

use crate::Position;

pub struct XState {
    root: Window,
    conn: Connection,
}

// Struct basic implementations, I know it technically isn't correct but it works for my usecase :D
impl PartialEq for XState {
    fn eq(&self, other: &Self) -> bool {
        self.root == other.root
    }
    fn ne(&self, other: &Self) -> bool {
        self.root != other.root
    }
}

impl Eq for XState {}

impl PartialOrd for XState {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for XState {
    fn cmp(&self, other: &Self) -> Ordering {
        self.root.cmp(&other.root)
    }
}

impl Debug for XState {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Debug placeholder") // TODO: Implement nice debug display for window, Connection doesn't have debug so that can be skipped!
    }
}

impl XState {
    /// Create new XState object, **will panic on failure!**
    pub fn setup() -> Self {
        let (conn, screen_num) =
            xcb::Connection::connect(None).expect("Failed to get X11 connection");

        let setup = conn.get_setup();
        let screen = setup.roots().nth(screen_num as usize).expect(&format!(
            "Screen number {} wasn't found",
            screen_num as usize
        ));
        let root = screen.root();

        Self { conn, root }
    }

    /// Get **absolute** position
    pub fn get_position_absolute(&self) -> Result<Position, String> {
        let cookie = self.conn.send_request(&QueryPointer { window: self.root });
        match self.conn.wait_for_reply(cookie) {
            Ok(retval) => Ok(Position(retval.root_x() as usize, retval.root_y() as usize)),
            Err(e) => Err(e.to_string()),
        }
    }

    /// Get **absolute** position
    ///
    /// **Without error handling, will panic on failure**
    pub fn get_position_absolute_unsafe(&self) -> Position {
        let cookie = self.conn.send_request(&QueryPointer { window: self.root });
        let retval = self
            .conn
            .wait_for_reply(cookie)
            .expect("Absolute pointer location wasn't available");
        Position(retval.root_x() as usize, retval.root_y() as usize)
    }

    /// Set **absolute** position to **pos**
    ///
    /// When *relative* is enabled:
    /// > Set position **relative** to pointer by **pos**
    pub fn set_position(&self, pos: Position, relative: bool) -> Result<(), String> {
        let cookie = self.conn.send_request_checked(&WarpPointer {
            src_window: Window::none(), // None makes it global
            src_x: 0,
            src_y: 0,
            src_height: 0,
            src_width: 0,
            dst_window: if relative { Window::none() } else { self.root },
            dst_x: pos.0 as i16,
            dst_y: pos.1 as i16,
        });
        match self.conn.check_request(cookie) {
            Err(e) => Err(e.to_string()),
            _ => Ok(()),
        }
    }

    /// hold pointer button
    /// TODO: finish
    pub fn hold(&self) {
        self.conn.send_request(&GrabButton {
            owner_events: true,
            grab_window: self.root,
            event_mask: EventMask::empty(),
            pointer_mode: xcb::x::GrabMode::Sync,
            keyboard_mode: xcb::x::GrabMode::Async,
            confine_to: Window::none(),
            cursor: Cursor::none(),
            button: ButtonIndex::N1,
            modifiers: ModMask::empty()
        });
    }
}
