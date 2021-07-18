#![feature(proc_macro_hygiene, decl_macro)]

use rocket::http::Status;

#[macro_use]
extern crate rocket;
extern crate rocket_contrib;

#[post("/heartbeat")]
pub fn heartbeat() -> Status {
    Status::Ok
}

fn main() {
    rocket::ignite()
        .mount("/api/betch/",
        routes![
            heartbeat
            ],
        )
        .launch();
}