let booked_parking_space = 1

function sendBookingRequest(parking_space_id){
    booking_api_url = "http://localhost:8000/booking/" + parking_space_id.toString()
    var xmlHttp = new XMLHttpRequest()
    xmlHttp.open("POST", booking_api_url, true)
    params = "data=" + parking_space_id
    xmlHttp.send(null)
    console.log("SENT BOOKING GET REQUEST")
    return xmlHttp.responseText
}

let booking_btn = document.getElementById("book_btn")
booking_btn.addEventListener('click', event => {
    sendBookingRequest(booked_parking_space)
})

function setParkingBooked(btn_handle, parking_space){
    btn_handle.style.backgroundColor = "salmon"
    btn_handle.style.color = "white"
    console.log("Setting button " + booked_parking_space + " as booked")
}

let a1_btn = document.getElementById("parking_space_a1")
let a2_btn = document.getElementById("parking_space_a2")
let a3_btn = document.getElementById("parking_space_a3")
let a4_btn = document.getElementById("parking_space_a4")
let a5_btn = document.getElementById("parking_space_a5")
let a6_btn = document.getElementById("parking_space_a6")
let a7_btn = document.getElementById("parking_space_a7")
let a8_btn = document.getElementById("parking_space_a8")

a1_btn.addEventListener('click', event => {
    setParkingBooked(a1_btn)
    booked_parking_space = 1
})
a2_btn.addEventListener('click', event => {
    setParkingBooked(a2_btn)
    booked_parking_space = 2
})
a3_btn.addEventListener('click', event => {
    setParkingBooked(a3_btn)
    booked_parking_space = 3
})
a4_btn.addEventListener('click', event => {
    setParkingBooked(a4_btn)
    booked_parking_space = 4
})
a5_btn.addEventListener('click', event => {
    setParkingBooked(a5_btn)
    booked_parking_space = 5
})
a6_btn.addEventListener('click', event => {
    setParkingBooked(a6_btn)
    booked_parking_space = 6
})
a7_btn.addEventListener('click', event => {
    setParkingBooked(a7_btn)
    booked_parking_space = 7
})
a8_btn.addEventListener('click', event => {
    setParkingBooked(a8_btn)
    booked_parking_space = 8
})



