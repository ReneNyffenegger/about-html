var video;

function startWebCam() {

// video = document.createElement( 'video');
   video = document.querySelector('#video');

   video.style.width  = '400px'; // document.body.clientWidth  + 'px';
// video.style.height = '400px'; // document.body.clientHeight + 'px';

   video.setAttribute('autoplay'   , 'true');

// document.body.appendChild(video);

   var stopVideo = document.querySelector("#stop");

   if (navigator.mediaDevices.getUserMedia) {
     navigator.mediaDevices.getUserMedia({ video: true })
       .then(function(stream) {
         video.srcObject = stream;
       })
       .catch (function(err) {
         alert(err);
       });
   }

   stopVideo.addEventListener("click", stopWebcam, false);
}

function stopWebcam(ev) {
   var tracks = video.srcObject.getTracks();

   for (var i = 0; i < tracks.length; i++) {

     tracks[i].stop();
   }

   video.srcObject = null;
}
