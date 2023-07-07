```javascript
let user = null;
let video = null;
let meme = null;

document.getElementById('video-upload').addEventListener('change', uploadVideo);
document.getElementById('segment-select').addEventListener('change', selectSegment);
document.getElementById('caption-text').addEventListener('input', addCaption);
document.getElementById('effect-select').addEventListener('change', applyEffect);
document.getElementById('export-button').addEventListener('click', exportMeme);

function uploadVideo(event) {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('video', file);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        video = data;
        console.log('videoUploaded');
    })
    .catch(error => console.error('Error:', error));
}

function selectSegment(event) {
    const segment = event.target.value;
    fetch(`/selectSegment?video=${video.id}&segment=${segment}`)
    .then(response => response.json())
    .then(data => {
        video = data;
        console.log('segmentSelected');
    })
    .catch(error => console.error('Error:', error));
}

function addCaption(event) {
    const caption = event.target.value;
    fetch(`/addCaption?video=${video.id}&caption=${caption}`)
    .then(response => response.json())
    .then(data => {
        meme = data;
        console.log('captionAdded');
    })
    .catch(error => console.error('Error:', error));
}

function applyEffect(event) {
    const effect = event.target.value;
    fetch(`/applyEffect?meme=${meme.id}&effect=${effect}`)
    .then(response => response.json())
    .then(data => {
        meme = data;
        console.log('effectApplied');
    })
    .catch(error => console.error('Error:', error));
}

function exportMeme() {
    fetch(`/exportMeme?meme=${meme.id}`)
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'meme.mp4';
        a.click();
        console.log('memeExported');
    })
    .catch(error => console.error('Error:', error));
}
```