function copyToClipboard(elementId) {
    var tempInput = document.createElement("textarea");
    tempInput.value = document.getElementById(elementId).innerText;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
    alert('Copied: ' + tempInput.value);
}

function copyAllResults() {
    var resultsText = document.getElementById("result4d").innerText + "\n" +
                      document.getElementById("result3d").innerText + "\n" +
                      document.getElementById("result2d").innerText;

    var tempInput = document.createElement("textarea");
    tempInput.value = resultsText;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);

    alert('Copied all results:\n' + resultsText);
}

function clearResults() {
    document.getElementById("result4d").innerText = "";
    document.getElementById("result3d").innerText = "";
    document.getElementById("result2d").innerText = "";
    
    document.querySelector(".result h2:nth-of-type(1) + p").innerText = "";
    document.querySelector(".result h2:nth-of-type(2) + p").innerText = "";

    document.querySelector("input[name='url']").value = "https://www.belatiaksara4d.com/wapsecure/numberlocation.html";
    document.querySelector("input[name='jumlah_kombinasi']").value = "";
    document.querySelector("input[name='ai']").value = "";
    document.querySelector("input[name='am1']").value = "";
    document.querySelector("input[name='am2']").value = "";
}
