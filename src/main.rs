use std::thread;
use std::time::Duration;
 
use mouce::{Mouse, MouseActions};
 
fn main() {
    let mouse_manager = Mouse::new();
    let _ = mouse_manager.move_to(1000,1000);
}