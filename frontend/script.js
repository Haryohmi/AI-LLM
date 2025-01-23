async function getSummary() {
    const videoUrl = document.getElementById("videoUrl").value.trim();

    if (!videoUrl) {
        alert("Please enter a valid YouTube URL!");
        return;
    }

    try {
        console.log("calling backend");
        const response = await fetch("http://127.0.0.1:5000/get_summary", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ video_url: videoUrl })
        });
        console.log("response", response);

        const data = await response.json();

        if (data.status === "success") {
            document.getElementById("summarySection").classList.remove("hidden");
            document.getElementById("summary").innerText = data.summary;

            document.getElementById("questionInput").value = "";
        } else {
            alert("Failed to generate summary: " + data.message);
        }
    } catch (error) {
        alert("An error occurred: " + error.message);
    }
}

async function askQuestion() {
    const question = document.getElementById("questionInput").value.trim();

    if (!question) {
        alert("Please enter a valid Question!");
        return;
    }

    try {
        console.log("Asking question");
        const response = await fetch("http://127.0.0.1:5000/get_answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });
        console.log("response", response);

        const data = await response.json();

        if (data.status === "success") {
            document.getElementById("answerSection").classList.remove("hidden");
            document.getElementById("response").innerText = data.answer;

            document.getElementById("questionInput").value = "";
        } else {
            alert("Failed to generate Response: " + data.message);
        }
    } catch (error) {
        alert("An error occurred: " + error.message);
    }
}

function autoResizeTextarea(textarea) {
    textarea.style.height = "auto"; 
    textarea.style.height = textarea.scrollHeight + "px"; 
}

document.getElementById("summary").addEventListener("input", function () {
    autoResizeTextarea(this);
});

document.getElementById("response").addEventListener("input", function () {
    autoResizeTextarea(this);
});

document.getElementById("videoUrl").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        getSummary(); 
    }
});

document.getElementById("questionInput").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        askQuestion();
    }
});