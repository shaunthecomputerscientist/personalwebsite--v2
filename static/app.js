const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});












const bubbleContainer = document.querySelector('.bubble-container');

function createBubbles() {
  const numBubbles = 20;

  for (let i = 0; i < numBubbles; i++) {
    const bubble = document.createElement('div');
    bubble.className = `bubble ${i % 2 ? 'red' : 'blue'}`;
    bubble.style.left = `${Math.random() * 100}%`;
    bubble.style.right = `${Math.random() * 100}%`;
    bubble.style.animationDelay = `${Math.random() * 10}s`;
    bubbleContainer.appendChild(bubble);
  }
}

createBubbles();





/*document.addEventListener('DOMContentLoaded',function(){
    var robotImage=document.getElementById('robot-image')
    var audioPlayer=document.getElementById('audioplayer')
    var isPlaying=false;
    robotImage.addEventListener('click',function(){

      if(isPlaying){
        audioPlayer.pause();
        isPlaying=false;
      }
      else{
        audioPlayer.play();
        isPlaying=true;
      }

      
    });
});








document.addEventListener('DOMContentLoaded', function() {
  var myElements = document.querySelectorAll('.my-element');

  myElements.forEach(function(element){
    var playic = document.getElementById('play-icon');
    var pauseic = document.getElementById('pause-icon');

    element.addEventListener('click', function() {
      if (playic.classList.contains('active')) {
        playic.classList.remove('active');
        pauseic.classList.add('active');
      } else {
        playic.classList.add('active');
        pauseic.classList.remove('active');
      }



    });

  
  });
});*/


/*document.addEventListener('DOMContentLoaded', function() {
  var playIcon = document.getElementById('play-icon');
  var pauseIcon = document.getElementById('pause-icon');
  var audioPlayer = document.getElementById('audioplayer');

  playIcon.addEventListener('click', function() {
    audioPlayer.play();
    playIcon.classList.remove('active');
    pauseIcon.classList.add('active');
  });

  pauseIcon.addEventListener('click', function() {
    audioPlayer.pause();
    pauseIcon.classList.remove('active');
    playIcon.classList.add('active');
  });
});*/





document.addEventListener('DOMContentLoaded', function() {
  var playIcon = document.getElementById('play-icon');
  var pauseIcon = document.getElementById('pause-icon');
  var audioPlayer = document.getElementById('audioplayer');
  var trackButtons = document.querySelectorAll('.track-button');
  pauseAudio()
  var audioTracks = [
    { name: 'to the moon main theme by Laura Shigihara', src: '/static/music/27 To the Moon  - Piano (Ending Version).mp3' },
    { name: 'Track 2', src: '/static/music/21 Once Upon a Memory.mp3' },
    { name: 'Track 3', src: '/static/music/31 Trailer Theme - Part 2 (Instrumental).mp3' }
    // Add more audio tracks as needed
  ];

  var currentTrackIndex = 0;

  function loadAudio() {
    var currentTrack = audioTracks[currentTrackIndex];
    audioPlayer.src = currentTrack.src;
    audioPlayer.load();
  }

  function playAudio() {
    audioPlayer.play();
    playIcon.classList.remove('active');
    pauseIcon.classList.add('active');
  }

  function pauseAudio() {
    audioPlayer.pause();
    pauseIcon.classList.remove('active');
    playIcon.classList.add('active');
  }




  function changeTrack(trackIndex) {
    if (trackIndex === currentTrackIndex) {
      return; // Do nothing if the same track is clicked
    }
    pauseAudio();
    currentTrackIndex = trackIndex;
    loadAudio();
    playAudio();
  }




  playIcon.addEventListener('click', function() {
    playAudio();
  });

  pauseIcon.addEventListener('click', function() {
    pauseAudio();
  });



  trackButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var trackIndex = parseInt(button.getAttribute('data-index'), 10);
      changeTrack(trackIndex);
    });
  });


  audioPlayer.addEventListener('ended', function() {
    pauseAudio();
    currentTrackIndex = (currentTrackIndex + 1) % audioTracks.length;
    loadAudio();
    playAudio();
  });

  loadAudio();
});

