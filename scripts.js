 		// Automatic Slideshow - change image every 3 seconds
			var myIndex = 0;
			carousel();
			
			function carousel() {
			    var i;
			    var x = document.getElementsByClassName("mySlides");
			    for (i = 0; i < x.length; i++) {
			        x[i].style.display = "none";
			    }
			    myIndex++;
			    if (myIndex > x.length) {myIndex = 1}
			    x[myIndex-1].style.display = "block";
			    setTimeout(carousel, 3000);
			}
		//Play/Pause Button
			function aud_play_pause() {
			  var myaudio = document.getElementById("myaudio");
			  if (myaudio.paused) {
			    myaudio.play();
			  } else {
			    myaudio.pause();
			  }
			}
		//Random Songs
				var sounds = new Array();
				sounds[0]="TouchMyBody.mp3";
				sounds[1]="Single.mp3";
				sounds[2]="Emotions.mp3"; 
				sounds[3]="Primadonna.mp3";
				sounds[4]="Froot.m4a";
				
				function getRandomSounds() {
				    var randomNum = Math.floor(Math.random()*sounds.length);
				    document.getElementById("myaudio").src = sounds[randomNum];
				}
				getRandomSounds();