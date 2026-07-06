// ==========================================
// KrishiMitra AI Voice Assistant
// ==========================================

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const askBtn = document.getElementById("askBtn");

const question = document.getElementById("question");
const responseBox = document.getElementById("response");
const statusBox = document.getElementById("status");
const language = document.getElementById("language");

// ==========================================
// Speech Recognition
// ==========================================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

let recognition = null;

if (SpeechRecognition) {

    recognition = new SpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    // ======================================
    // Start Recognition
    // ======================================

    startBtn.addEventListener("click", () => {

        recognition.lang = language.value;

        recognition.start();

    });

    // ======================================
    // Stop Recognition
    // ======================================

    stopBtn.addEventListener("click", () => {

        recognition.stop();

    });

    // ======================================
    // Listening Started
    // ======================================

    recognition.onstart = () => {

        startBtn.classList.add("listening");

        statusBox.className = "alert alert-success";

        statusBox.innerHTML = "🎤 Listening... Please speak.";

    };

    // ======================================
    // Speech Result
    // ======================================

    recognition.onresult = (event) => {

        const transcript = event.results[0][0].transcript;

        console.log("You said:", transcript);

        question.value = transcript;

        statusBox.className = "alert alert-success";

        statusBox.innerHTML = "✅ Voice captured successfully.";

    };

    // ======================================
    // Recognition End
    // ======================================

    recognition.onend = () => {

        startBtn.classList.remove("listening");

        statusBox.className = "alert alert-secondary";

        statusBox.innerHTML = "Microphone stopped.";

    };

    // ======================================
    // Error
    // ======================================

    recognition.onerror = (event) => {

        console.log(event.error);

        startBtn.classList.remove("listening");

        statusBox.className = "alert alert-danger";

        switch(event.error){

            case "no-speech":
                statusBox.innerHTML = "No speech detected.";
                break;

            case "audio-capture":
                statusBox.innerHTML = "Microphone not found.";
                break;

            case "not-allowed":
                statusBox.innerHTML = "Microphone permission denied.";
                break;

            default:
                statusBox.innerHTML = event.error;

        }

    };

}
else{

    statusBox.className = "alert alert-danger";

    statusBox.innerHTML =
    "Speech Recognition is not supported in this browser.";

}

// ==========================================
// Speak Response
// ==========================================

function speak(text){

    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = language.value;

    speech.rate = 1;

    speech.pitch = 1;

    speech.volume = 1;

    window.speechSynthesis.speak(speech);

}

// ==========================================
// Ask AI
// ==========================================

async function askAI(){

    const text = question.value.trim();

    if(text===""){

        alert("Please ask a question.");

        return;

    }

    responseBox.innerHTML = `
        <div class="text-center p-4">

            <div class="spinner-border text-success"></div>

            <br><br>

            Thinking...

        </div>
    `;

    try{

        const response = await fetch("/voice-chat",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                question:text,

                language:language.value

            })

        });

        const data = await response.json();

        console.log(data);

        if(data.error){

            responseBox.innerHTML=`
                <div class="alert alert-danger">
                    ${data.error}
                </div>
            `;

            return;

        }

        responseBox.innerHTML=`
            <div class="alert alert-success">

                ${data.answer.replace(/\n/g,"<br>")}

            </div>
        `;

        speak(data.answer);

    }

    catch(error){

        console.log(error);

        responseBox.innerHTML=`
            <div class="alert alert-danger">

                Server Error.

            </div>
        `;

    }

}

// ==========================================
// Events
// ==========================================

askBtn.addEventListener("click", askAI);

question.addEventListener("keypress", function(e){

    if(e.key==="Enter" && !e.shiftKey){

        e.preventDefault();

        askAI();

    }

});