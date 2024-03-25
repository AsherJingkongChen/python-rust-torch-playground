fn main() {
    if cfg!(target_family = "unix") {
        println!(r"cargo:rustc-link-search=native=/usr/lib");
    }
}
