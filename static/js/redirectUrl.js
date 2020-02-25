const redirectUrlText = (text,redirect) => {
    document.getElementById("redirectUrlText").innerHTML = "";
    document.getElementById("redirect-url-overlay").classList.remove("none");
    var textDisplayArr = text.split("");
    var RedirectTextDelay = 1.5;
    var RedirectGPdelay = 0.05;
    for (var i = 0;i<textDisplayArr.length;i++){
        var newElmt = document.createElement("div");
        if (text.length > 9){
            newElmt.className = "redirectText1";
        }
        else{
            newElmt.className = "redirectText";
        }
        newElmt.style.animationDelay = `${RedirectTextDelay + i * RedirectGPdelay}s`;
        newElmt.innerText = textDisplayArr[i];
        document.getElementById("redirectUrlText").appendChild(newElmt);
    }
    if (redirect != ""){
        setTimeout(() => {
            window.location = `/${redirect}`;
        }, 3000);
    }
    else{
        setTimeout(() => {
            document.getElementById("redirect-url-overlay").classList.add("ScaleDownAll");
        }, 3500);
        setTimeout(()=>{
            document.getElementById("redirect-url-overlay").classList.add("none");
            document.getElementById("redirect-url-overlay").classList.remove("ScaleDownAll");
        },5000);
    }
}