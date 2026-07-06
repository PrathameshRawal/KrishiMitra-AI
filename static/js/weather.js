// ==========================================
// KrishiMitra AI Weather Intelligence
// ==========================================

const cityInput = document.getElementById("city");
const searchBtn = document.getElementById("searchBtn");

const locationText = document.getElementById("location");
const temperature = document.getElementById("temperature");
const condition = document.getElementById("condition");

const humidity = document.getElementById("humidity");
const wind = document.getElementById("wind");
const feels = document.getElementById("feels");

const rain = document.getElementById("rain");
const rainProbability = document.getElementById("rainProbability");
const visibility = document.getElementById("visibility");
const sunrise = document.getElementById("sunrise");
const sunset = document.getElementById("sunset");

const advice = document.getElementById("advice");

// ==========================================
// Fetch Weather
// ==========================================

async function getWeather() {

    const city = cityInput.value.trim();

    if (city === "") {
        alert("Please enter a city.");
        return;
    }

    advice.innerHTML = `
        <div class="loading text-center">
            <div class="spinner-border text-success"></div>
            <p class="mt-3">Fetching Weather...</p>
        </div>
    `;

    try {

        const response = await fetch("/weather-data", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                city: city
            })

        });

        const data = await response.json();

        if (data.error) {

            advice.innerHTML = `
                <div class="alert alert-danger">
                    ${data.error}
                </div>
            `;

            return;
        }

        // --------------------------
        // Weather Details
        // --------------------------

        locationText.innerHTML = `📍 ${data.city}`;
        temperature.innerHTML = `${data.temperature}°C`;
        condition.innerHTML = data.condition;

        humidity.innerHTML = `${data.humidity}%`;
        wind.innerHTML = `${data.wind} km/h`;
        feels.innerHTML = `${data.feels_like}°C`;

        rain.innerHTML = data.rainfall;
        rainProbability.innerHTML = data.rain_probability;

        visibility.innerHTML = data.visibility;

        sunrise.innerHTML = data.sunrise;
        sunset.innerHTML = data.sunset;

        // --------------------------
        // AI Advice
        // --------------------------

        advice.innerHTML = `
            <div class="alert alert-success">
                ${data.ai_advice.replace(/\n/g, "<br>")}
            </div>
        `;

    }

    catch (error) {

        console.error(error);

        advice.innerHTML = `
            <div class="alert alert-danger">
                Unable to fetch weather data.
            </div>
        `;
    }

}

// ==========================================
// Events
// ==========================================

searchBtn.addEventListener("click", getWeather);

cityInput.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {
        getWeather();
    }

});

// ==========================================
// Default Weather
// ==========================================

// Uncomment if you want Pune weather to load automatically
// window.onload = function () {
//     cityInput.value = "Pune";
//     getWeather();
// };