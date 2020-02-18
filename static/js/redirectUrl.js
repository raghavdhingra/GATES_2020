const redirectUrlText = (text,redirect) => {
    document.getElementById("redirect-url-overlay").classList.remove("none");
    var textDisplayArr = text.split("");
    var textDisplay = "";
    for (var i = 0;i<textDisplayArr.length;i++){
        var intermediateText = `<div class="redirectText">${textDisplayArr[i]}</div>`;
        textDisplay+=intermediateText;
    }
    console.log(textDisplay);
    document.getElementById("redirectUrlText").innerHTML = textDisplay;
    setTimeout(() => {
        window.location = `/${redirect}`;
    }, 3000);
}