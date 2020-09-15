let canvas = document.createElement("canvas");
let ctx = canvas.getContext("2d");


document.getElementById('file').onchange = function(evt) {
    let tgt = evt.target || window.event.srcElement,
        files = tgt.files;


    // FileReader support
    if (FileReader && files && files.length) {
        let fr = new FileReader();
        fr.onload = () => showImage(fr);
        fr.readAsDataURL(files[0]);
    }
}

function showImage(fileReader) {
    let img = document.getElementById("myImage");
    img.onload = () => getImageData(img);
    img.src = fileReader.result;
    //saveImage2Server(img.src);
    runTensorFlow(img);

}

function getImageData(img) {
    ctx.drawImage(img, 0, 0);
    imageData = ctx.getImageData(0, 0, img.width, img.height).data;
    console.log("image data:", imageData);
}


