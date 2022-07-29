<script>

function randomNumber() {
    let x= Math.floor(Math.random()*1000000000000000)
    return x
}
setInterval(randomNumber,2000)
let xNo= randomNumber()

function getNumber() {
    console.log(xNo);
}
getNumber()

document.getElementById("head").innerHTML = xNo
document.getElementById("link").href = xNo
    
    </script>
