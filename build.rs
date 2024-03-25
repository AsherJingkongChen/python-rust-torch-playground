use std::env::consts::ARCH;

fn main() {
    if cfg!(target_family = "unix") {
        println!(r"cargo:rustc-link-search=native=/lib");
        println!(r"cargo:rustc-link-search=native=/usr/lib");
        println!(r"cargo:rustc-link-search=native=/usr/local/lib");
    }
    if cfg!(target_os = "linux") {
        println!(r"cargo:rustc-link-search=native=/lib/{ARCH}-linux-gnu");
        println!(r"cargo:rustc-link-search=native=/usr/lib/{ARCH}-linux-gnu");
    }
}
