/* rollover.js */

window.onload = rolloverInit;

function rolloverInit() {
	console.log("called function")
	for (var i=0; i<document.images.length; i++) {
		console.log("in for loop")
		if (document.images[i].parentNode.tagName == "A") {
			console.log ("in if")
			setupRollover(document.images[i]);
			console.log ("init setup function")
		}
	}
}
	
	function setupRollover(thisImage){
		thisImage.outImage = new Image();
		thisImage.outImage.src = "buttons/" + thisImage.id + ".png"
		thisImage.onmouseout = rollOut;

		console.log("getting roll out")
		
		thisImage.overImage = new Image();
		thisImage.overImage.src = "buttons/" + thisImage.id + "_rollover.png"
		thisImage.onmouseover = rollOver;	
		console.log("getting over")

		thisImage.clickImage = new Image();
		thisImage.clickImage.src = "buttons/" + thisImage.id + "_click.png"
		thisImage.onclick = rollClick;	
		console.log("getting click")
	}
	
	function rollOver(){
		this.src = this.overImage.src
		console.log("get rollOver")
	}
	
	function rollOut(){
		this.src= this.outImage.src
		console.log("get rollOut")
	}
	
	function rollClick (){
		this.src = this.clickImage.src
		console.log("get rollClick")

	}