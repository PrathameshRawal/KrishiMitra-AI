async function generateCalendar() {

    const cropValue = crop.value;
    const stateValue = state.value;

    if (cropValue === "" || stateValue === "") {
        alert("Please select Crop and State.");
        return;
    }

    loading.classList.remove("d-none");

    result.innerHTML = "";

    calendarBtn.disabled = true;
    calendarBtn.innerHTML = "Generating...";

    try {

        const response = await fetch("/generate_crop_calendar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                crop: cropValue,
                state: stateValue
            })
        });

        const data = await response.json();

        loading.classList.add("d-none");

        calendarBtn.disabled = false;
        calendarBtn.innerHTML = "Generate Calendar";

        if (data.error) {
            result.innerHTML =
                `<div class="alert alert-danger">${data.error}</div>`;
            return;
        }

        const html = data.calendar
            .replace(/🌱/g, "<h4>🌱")
            .replace(/🌾/g, "<h4>🌾")
            .replace(/💧/g, "<h4>💧")
            .replace(/🧪/g, "<h4>🧪")
            .replace(/🌿/g, "<h4>🌿")
            .replace(/🐛/g, "<h4>🐛")
            .replace(/✂/g, "<h4>✂")
            .replace(/📦/g, "<h4>📦")
            .replace(/💰/g, "<h4>💰")
            .replace(/----------------------------------/g, "<hr>")
            .replace(/\n/g, "<br>");

        result.innerHTML =
            `<div class="calendar-card">${html}</div>`;

    }

    catch (error) {

        loading.classList.add("d-none");

        calendarBtn.disabled = false;
        calendarBtn.innerHTML = "Generate Calendar";

        result.innerHTML =
            `<div class="alert alert-danger">Something went wrong.</div>`;

        console.log(error);

    }

}

calendarBtn.addEventListener("click", generateCalendar);