let chooseFileButton = document.getElementById("chooseFile");
let sendFileButton = document.getElementById("sendFile");
sendFileButton.disabled = true;
sendFileButton.classList.remove("mainButton")

chooseFileButton.addEventListener("change", selectFile);

function selectFile() {
    const file = this.files[0];
    if (file) {
        sendFileButton.disabled = false;
        sendFileButton.classList.add("mainButton")
    }
    else {
        sendFileButton.disabled = true;
        sendFileButton.classList.remove("mainButton")
    }
}