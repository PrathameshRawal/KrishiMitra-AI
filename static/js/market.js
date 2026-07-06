// ==========================================
// KrishiMitra AI - Market Prices
// ==========================================

const cropInput = document.getElementById("crop");
const searchBtn = document.getElementById("searchBtn");

const table = document.getElementById("marketTable");
const advice = document.getElementById("advice");

// ==========================================
// Search Market Prices
// ==========================================

async function searchMarket() {

    const crop = cropInput.value.trim();

    if (crop === "") {
        alert("Please enter a crop name.");
        return;
    }

    table.innerHTML = `
        <tr>
            <td colspan="8" class="text-center">
                <div class="spinner-border text-success"></div>
                <br><br>
                Loading market prices...
            </td>
        </tr>
    `;

    advice.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-success"></div>
            <br><br>
            Generating AI advice...
        </div>
    `;

    try {

        const response = await fetch("/market-prices", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                crop: crop
            })
        });

        const data = await response.json();

        if (data.error) {

            table.innerHTML = `
                <tr>
                    <td colspan="8" class="text-danger text-center">
                        ${data.error}
                    </td>
                </tr>
            `;

            advice.innerHTML = `
                <div class="alert alert-danger">
                    ${data.error}
                </div>
            `;

            return;
        }

        // ================================
        // Fill Table
        // ================================

        table.innerHTML = "";

        data.prices.forEach(item => {

            table.innerHTML += `
                <tr>
                    <td>${item.crop}</td>
                    <td>${item.state}</td>
                    <td>${item.district}</td>
                    <td>${item.market}</td>
                    <td>${item.arrival_date}</td>
                    <td>₹${item.min_price}</td>
                    <td>₹${item.max_price}</td>
                    <td>₹${item.modal_price}</td>
                </tr>
            `;

        });

        // ================================
        // AI Advice
        // ================================

        advice.innerHTML = `
            <div class="alert alert-success">
                ${data.ai_advice.replace(/\n/g, "<br>")}
            </div>
        `;

    } catch (error) {

        console.error(error);

        table.innerHTML = `
            <tr>
                <td colspan="8" class="text-danger text-center">
                    Unable to fetch market prices.
                </td>
            </tr>
        `;

        advice.innerHTML = `
            <div class="alert alert-danger">
                Server Error.
            </div>
        `;
    }
}

// ==========================================
// Events
// ==========================================

searchBtn.addEventListener("click", searchMarket);

cropInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        searchMarket();
    }
});