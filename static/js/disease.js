// ==========================================
// KrishiMitra AI Disease Detection
// ==========================================

const imageInput = document.getElementById("imageInput");
const chooseImage = document.getElementById("chooseImage");
const preview = document.getElementById("preview");

const diseaseForm = document.getElementById("diseaseForm");

const loading = document.getElementById("loading");
const result = document.getElementById("result");

// ------------------------------------
// Choose Image
// ------------------------------------

chooseImage.addEventListener("click", () => {

    imageInput.click();

});

// ------------------------------------
// Preview Image
// ------------------------------------

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) return;

    const reader = new FileReader();

    reader.onload = function (e) {

        preview.src = e.target.result;

    };

    reader.readAsDataURL(file);

});

// ------------------------------------
// Submit
// ------------------------------------

diseaseForm.addEventListener("submit", async function (e) {

    e.preventDefault();

    const file = imageInput.files[0];

    if (!file) {

        alert("Please select an image.");

        return;

    }

    const formData = new FormData();

    formData.append("image", file);

    loading.classList.remove("d-none");

    result.innerHTML = "";

    try {

        const response = await fetch("/detect-disease", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        loading.classList.add("d-none");

        result.innerHTML = `

<div class="result-item">

<h5>🌿 Disease</h5>

<p>${data.disease}</p>

</div>

<div class="result-item">

<h5>📊 Confidence</h5>

<p>${data.confidence}</p>

</div>

<div class="result-item">

<h5>🦠 Cause</h5>

<p>${data.cause}</p>

</div>

<div class="result-item">

<h5>🌱 Organic Treatment</h5>

<p>${data.organic}</p>

</div>

<div class="result-item">

<h5>💊 Chemical Treatment</h5>

<p>${data.chemical}</p>

</div>

<div class="result-item">

<h5>🛡 Prevention</h5>

<p>${data.prevention}</p>

</div>

`;

    }

    catch (err) {

        loading.classList.add("d-none");

        result.innerHTML = `

<div class="alert alert-danger">

Unable to analyze image.

Please try again.

</div>

`;

        console.error(err);

    }

});