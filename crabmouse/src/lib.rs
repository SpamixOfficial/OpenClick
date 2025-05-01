#[cfg(feature = "linux")]
pub mod linux;
#[cfg(feature = "macos")]
pub mod macos;
#[cfg(feature = "windows")]
pub mod windows;

use std::ops::{Add, Sub};

#[derive(Debug, Copy, Clone, PartialEq)]
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
    fn set_position(&mut self, pos: Position) {
        unimplemented!()
    }
    /// Get current position
    fn get_position(&mut self) {
        unimplemented!()
    }
    /// Set relative position, aka "move relative"
    /// Example: move_relative(Position(1,1)) would move it x+1 and y+1
    fn move_relative(&mut self, pos: Position) {
        unimplemented!()
    }
    /// Simulate click
    fn click(&mut self, click: Click) {
        unimplemented!()
    }
    // TODO: Simulate scoll
    //fn scroll(&mut self, scroll: Click){
    //    unimplemented!()
    //}
}
