// ==========================================
// KrishiMitra AI - Government Schemes
// ==========================================

const state = document.getElementById("state");
const category = document.getElementById("category");

const searchBtn = document.getElementById("searchBtn");

const loading = document.getElementById("loading");
const result = document.getElementById("result");
const aiAdvice = document.getElementById("aiAdvice");

// ==========================================
// Search Government Schemes
// ==========================================

async function searchSchemes() {

    const selectedState = state.value;
    const selectedCategory = category.value;

    if (selectedState === "" || selectedCategory === "") {

        alert("Please select State and Farmer Category.");

        return;

    }

    loading.classList.remove("d-none");

    result.innerHTML = "";

    aiAdvice.innerHTML = "";

    try {

        const response = await fetch("/get-schemes", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                state: selectedState,

                category: selectedCategory

            })

        });

        const data = await response.json();

        loading.classList.add("d-none");

        // ===============================
        // Error
        // ===============================

        if (data.error) {

            result.innerHTML = `

                <div class="alert alert-danger">

                    ${data.error}

                </div>

            `;

            return;

        }

        // ===============================
        // Show Schemes
        // ===============================

        result.innerHTML = "";

        data.schemes.forEach((scheme) => {

            result.innerHTML += `

                <div class="scheme-card">

                    <div class="scheme-title">

                        🌾 ${scheme.name}

                    </div>

                    <p>

                        <strong>Description:</strong>

                        ${scheme.description}

                    </p>

                    <p>

                        <strong>Eligibility:</strong>

                        ${scheme.eligibility}

                    </p>

                    <p>

                        <strong>Benefits:</strong>

                        ${scheme.benefits}

                    </p>

                </div>

            `;

        });

        // ===============================
        // AI Advice
        // ===============================

        aiAdvice.innerHTML = `

            <div class="alert alert-success">

                ${data.ai_advice.replace(/\n/g,"<br>")}

            </div>

        `;

    }

    catch (error) {

        console.error(error);

        loading.classList.add("d-none");

        result.innerHTML = `

            <div class="alert alert-danger">

                Unable to fetch government schemes.

            </div>

        `;

        aiAdvice.innerHTML = `

            <div class="alert alert-warning">

                AI explanation is unavailable.

            </div>

        `;

    }

}

// ==========================================
// Events
// ==========================================

searchBtn.addEventListener("click", searchSchemes);