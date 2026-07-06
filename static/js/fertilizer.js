// ==========================================
// KrishiMitra AI - Fertilizer Recommendation
// ==========================================

const crop = document.getElementById("crop");
const soil = document.getElementById("soil");
const stage = document.getElementById("stage");

const recommendBtn = document.getElementById("recommendBtn");

const loading = document.getElementById("loading");
const result = document.getElementById("result");

// ==========================================
// Generate Recommendation
// ==========================================

async function generateRecommendation() {

    const cropValue = crop.value;
    const soilValue = soil.value;
    const stageValue = stage.value;

    if (cropValue === "" || soilValue === "" || stageValue === "") {

        alert("Please fill all fields.");

        return;

    }

    loading.classList.remove("d-none");

    result.innerHTML = "";

    recommendBtn.disabled = true;
    recommendBtn.innerHTML = "Generating...";

    try {

        const response = await fetch("/fertilizer-recommendation", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                crop: cropValue,
                soil: soilValue,
                stage: stageValue

            })

        });

        const data = await response.json();

        loading.classList.add("d-none");

        recommendBtn.disabled = false;
        recommendBtn.innerHTML = "Generate Recommendation";

        if (data.error) {

            result.innerHTML = `

                <div class="alert alert-danger">

                    ${data.error}

                </div>

            `;

            return;

        }

        result.innerHTML = `

            <div class="alert alert-success">

                ${data.recommendation.replace(/\n/g,"<br>")}

            </div>

        `;

    }

    catch (error) {

        console.error(error);

        loading.classList.add("d-none");

        recommendBtn.disabled = false;
        recommendBtn.innerHTML = "Generate Recommendation";

        result.innerHTML = `

            <div class="alert alert-danger">

                Unable to generate fertilizer recommendation.

            </div>

        `;

    }

}

// ==========================================
// Event
// ==========================================

recommendBtn.addEventListener("click", generateRecommendation);