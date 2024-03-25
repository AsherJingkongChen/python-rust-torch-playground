#![feature(cfg_match)]

fn main() {
    cfg_match! {
        cfg(target_family = "unix") => {
            println!(r"cargo:rustc-link-search=native=/usr/lib");
        }
    }
}