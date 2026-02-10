// -------- Mock podatki --------
const driversTop5 = [
    "Max Verstappen",
    "Lewis Hamilton",
    "Charles Leclerc",
    "George Russell",
    "Sergio Perez"
];

const constructorsTop5 = [
    "Red Bull Racing",
    "Mercedes",
    "Ferrari",
    "McLaren",
    "Alpine"
];

const nextRaces = [
    "Monza - 07/09/2026",
    "Singapore - 21/09/2026",
    "Suzuka - 05/10/2026"
];

const lastRaceResults = [
    "1. Max Verstappen - 1:24:30.123",
    "2. Lewis Hamilton - 1:24:45.567",
    "3. Charles Leclerc - 1:25:10.890"
];

const news = [
    "Verstappen wins dramatic race!",
    "Mercedes introduces new car upgrade",
    "Ferrari struggles in qualifying"
];

// -------- Funkcija za render --------
function renderList(sectionId, items) {
    const ul = document.querySelector(`#${sectionId}`);
    ul.innerHTML = ""; // očisti predhodne elemente
    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
    });
}

// -------- Render vseh sekcij --------
renderList("drivers", driversTop5);
renderList("constructors", constructorsTop5);
renderList("next-races", nextRaces);
renderList("last-results", lastRaceResults);
renderList("news", news);