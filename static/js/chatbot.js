const chatBox = document.getElementById("chatBox");
const message = document.getElementById("message");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearChat");
const loading = document.getElementById("loadingMessage");

// =====================================
// Add Chat Message
// =====================================

function addMessage(sender, text) {

    const wrapper = document.createElement("div");

    wrapper.className = sender === "user"
        ? "user-message"
        : "bot-message";

    const avatar = document.createElement("div");
    avatar.className = "avatar";

    avatar.innerHTML = sender === "user"
        ? "👨‍🌾"
        : "🌱";

    const bubble = document.createElement("div");
    bubble.className = "message";

    bubble.innerHTML = `
        <strong>${sender === "user" ? "You" : "KrishiMitra AI"}</strong>
        <p>${text.replace(/\n/g, "<br>")}</p>
    `;

    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);

    chatBox.appendChild(wrapper);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// =====================================
// Send Message
// =====================================

async function sendMessage() {

    const text = message.value.trim();

    if (text === "") return;

    // Show user message
    addMessage("user", text);

    message.value = "";

    // Show loading
    loading.style.display = "flex";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: text
            })

        });

        const data = await response.json();

        // Hide loading
        loading.style.display = "none";

        if (data.reply) {

            addMessage("bot", data.reply);

        } else {

            addMessage(
                "bot",
                "Sorry, I couldn't generate a response."
            );

        }

    } catch (error) {

        console.error(error);

        loading.style.display = "none";

        addMessage(
            "bot",
            "⚠ Server error. Please try again."
        );

    }

}

// =====================================
// Send Button
// =====================================

sendBtn.addEventListener("click", sendMessage);

// =====================================
// Press Enter to Send
// Shift + Enter = New Line
// =====================================

message.addEventListener("keydown", function (e) {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

// =====================================
// Clear Chat
// =====================================

clearBtn.addEventListener("click", () => {

    chatBox.innerHTML = `

<div class="bot-message">

    <div class="avatar">
        🌱
    </div>

    <div class="message">

        <strong>KrishiMitra AI</strong>

        <p>

            Chat cleared successfully.

            <br><br>

            How can I help you today?

        </p>

    </div>

</div>

<div id="loadingMessage" class="bot-message" style="display:none;">

    <div class="avatar">
        🤖
    </div>

    <div class="message">

        <strong>KrishiMitra AI</strong>

        <p>

            <i class="fa-solid fa-spinner fa-spin"></i>

            Thinking...

            <br>

            Please wait while I generate the best farming advice.

        </p>

    </div>

</div>

`;

});