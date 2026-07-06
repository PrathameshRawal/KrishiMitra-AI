// ==========================================
// KrishiMitra AI - Crop Recommendation
// ==========================================

const form = document.getElementById("recommendForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const state = document.getElementById("state").value.trim();
    const district = document.getElementById("district").value.trim();
    const soil = document.getElementById("soil").value;
    const season = document.getElementById("season").value;
    const land = document.getElementById("land").value;

    result.innerHTML = `
        <div class="loading">
            <div class="spinner-border text-success"></div>
            <p class="mt-3">
                KrishiMitra AI is analyzing your farm...
            </p>
        </div>
    `;

    try {

        const response = await fetch("/recommend-crop", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                state: state,
                district: district,
                soil: soil,
                season: season,
                land: land

            })

        });

        const data = await response.json();

        if (data.error) {

            result.innerHTML = `
                <div class="alert alert-danger">
                    ${data.error}
                </div>
            `;

            return;
        }

        result.innerHTML = `
            <div class="result-box">

                <h5>
                    🌾 AI Crop Recommendation
                </h5>

                <div style="white-space:pre-line;">
                    ${data.recommendation}
                </div>

            </div>
        `;

    }

    catch (error) {

        console.error(error);

        result.innerHTML = `
            <div class="alert alert-danger">
                Unable to generate recommendation.
            </div>
        `;

    }

});