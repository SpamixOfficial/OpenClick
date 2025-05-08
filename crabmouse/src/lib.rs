#[cfg(all(target_os = "linux", feature = "linux"))]
pub mod linux;
#[cfg(all(target_os = "macos", feature = "macos"))]
pub mod macos;

#[cfg(all(target_os = "windows", feature = "windows"))]
pub mod windows;

use std::ops::{Add, AddAssign, Sub, SubAssign};

#[derive(Debug, Copy, Clone, PartialEq, Default)]
pub struct Position(usize, usize);

impl Position {
    pub fn new(x: usize, y: usize) -> Self {
        return Self(x, y);
    }
    pub fn set(&mut self, x: usize, y: usize) {
        self.0 = x;
        self.1 = y;
    }
}

impl AddAssign for Position {
    fn add_assign(&mut self, rhs: Self) {
        *self = Self(self.0 + rhs.0, self.1 + rhs.1);
    }
}

impl SubAssign for Position {
    fn sub_assign(&mut self, rhs: Self) {
        *self = Self(self.0 - rhs.0, self.1 - rhs.1);
    }
}

impl Add for Position {
    type Output = Self;
    fn add(self, b: Self) -> Self {
        Self(self.0 + b.0, self.1 + b.1)
    }
}

impl Sub for Position {
    type Output = Self;
    fn sub(self, b: Self) -> Self {
        Self(self.0 - b.0, self.1 - b.1)
    }
}

#[derive(Debug, Copy, Clone, PartialEq)]
pub enum Click {
    Right,
    Left,
    Middle,
}

pub trait MouseFeat {
    /// Set absolute position
    fn set_position(&self, pos: Position) -> Result<(), String> {
        unimplemented!()
    }
    /// Get current position
    fn get_position(&self) -> Result<Position, String> {
        unimplemented!()
    }
    /// Set relative position, aka "move relative"
    ///
    /// Example: move_relative(Position(1,1)) would move it x+1 and y+1
    fn set_relative_position(&self, pos: Position) -> Result<(), String> {
        unimplemented!()
    }
    /// Simulate single click
    fn click(&self, click: Click) -> Result<(), String> {
        unimplemented!()
    }

    /// Simulate holding click (no key-release)
    fn click_grab(&self, click: Click) -> Result<(), String> {
        unimplemented!()
    }

    /// Simulate release click (key-release)
    ///
    /// Usually only used after **click_grab**
    fn click_release(&self, click: Click) -> Result<(), String> {
        unimplemented!()
    }

    // TODO: Simulate scoll
    //fn scroll(&self, scroll: Click){
    //    unimplemented!()
    //}
}
