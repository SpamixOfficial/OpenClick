use std::env;
use std::path::PathBuf;

fn main() {
    if cfg!(target_os = "linux") {
        let uinput_bind = bindgen::Builder::default()
            .header("bindings/uinput.h")
            .parse_callbacks(Box::new(bindgen::CargoCallbacks::new()))
            .generate()
            .expect("Unable to generate bindings");

        let out_path = PathBuf::from("src/bindings/");
        uinput_bind
            .write_to_file(out_path.join("uinput.rs"))
            .expect("Couldn't write uinput-bindings!");
    }
}