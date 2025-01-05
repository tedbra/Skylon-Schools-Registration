

const today = new Date(); // create a new Date object with the current date and time
const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]; // an array of weekday names
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]; // an array of month names

const weekdayName = weekdays[today.getDay()]; // get the weekday name from the weekday array
const monthName = months[today.getMonth()]; // get the month name from the month array
const day = today.getDate(); // get the day of the month (1-31)
const year = today.getFullYear(); // get the year (4 digits)

const formattedDate = `${weekdayName}, ${monthName} ${day} ${year}`; // combine the parts into the desired format
const formattedDate2 = `${monthName} ${day} ${year}`; 
//console.log(formattedDate); // output the formatted date string


let myVariable = document.getElementById("today_date");
myVariable.innerHTML = formattedDate;

let myVariable2 = document.getElementById("the_date");
myVariable2.innerHTML = formattedDate2;


//document.getElementById('printButton').addEventListener('click', function() { window.print(); });
