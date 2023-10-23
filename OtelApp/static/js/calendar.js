let currentDate = new Date();
let currentMonth = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const datesInfo = [
  { date: "2023-10-03", room: 105, status: "reserve olundu" },
  { date: "2023-10-05", room: 106, status: "misafir var" },
  { date: "2023-11-05", room: 106, status: "misafir var" },
  { date: "2023-10-06", room: 106, status: "reserve olundu" },
];

document.addEventListener("DOMContentLoaded", () => {
  renderCalendar(currentMonth, currentYear);
});

function renderCalendar(month, year) {
  const firstDay = new Date(year, month).getDay();
  const daysInMonth = 32 - new Date(year, month, 32).getDate();
  const tableBody = document
    .getElementById("calendarTable")
    .getElementsByTagName("tbody")[0];
  tableBody.innerHTML = "";

  document.getElementById("currentMonthYear").innerText =
    monthNames[month] + " " + year;

  let date = 1;
  for (let week = 0; week < 6; week++) {
    let row = document.createElement("tr");
    for (let dayOfWeek = 0; dayOfWeek < 7; dayOfWeek++) {
      let cell = document.createElement("td");
      if ((week === 0 && dayOfWeek < firstDay) || date > daysInMonth) {
        cell.appendChild(document.createTextNode(""));
      } else {
        const dateString = `${year}-${String(month + 1).padStart(
          2,
          "0"
        )}-${String(date).padStart(2, "0")}`;
        let dateInfo = datesInfo.find((d) => d.date === dateString);
        if (dateInfo) {
          cell.className = dateInfo.status.replace(" ", "-").toLowerCase();
          cell.innerText =
            date + ": Room " + dateInfo.room + " (" + dateInfo.status + ")";
        } else {
          cell.innerText = date;
        }
        date++;
      }
      row.appendChild(cell);
    }
    tableBody.appendChild(row);
  }
}

function goToPreviousMonth() {
  if (currentMonth === 0) {
    currentMonth = 11;
    currentYear--;
  } else {
    currentMonth--;
  }
  renderCalendar(currentMonth, currentYear);
}

function goToNextMonth() {
  if (currentMonth === 11) {
    currentMonth = 0;
    currentYear++;
  } else {
    currentMonth++;
  }
  renderCalendar(currentMonth, currentYear);
}
