function dw(link){
    var check = document.getElementById('switch');
    if (check.checked == true){
        eel.ytP(link)();
        // alert("Progressive Download Initialized")
    } else {
        eel.ytH(link)();
        // alert("HighQuality Download Initialized"); //ffmpeg integration needed
    }
}

async function thumbnail(link){
    const thumb = await eel.thumb(link)();
    var img = document.createElement('img');
    img.src = thumb;
    var src = document.getElementById('streams'); 
    src.appendChild(img);
}

async function title(link){
    document.getElementById('status').innerHTML = await eel.showtitle(link)();
}

document.getElementById('btn').addEventListener('click', async() => {
    var link = document.getElementById('data').value;
    await title(link);
    await thumbnail(link);    
    dw(link);
})