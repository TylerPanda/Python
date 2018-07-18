function saySomething(phrase){
	console.log("You said: " + phrase)
}

function getPhraseLength(phrase, another){
	var l = phrase.length;

	// console.log(phrase);
	if(typeof another !== "undefined"){
		l += another.length;
	}

	function printBoth(){
		return phrase + " " + another;
	}
	return printBoth();
}

var p1 = "This is a slightly longer sentence.";
var p2 = "This is a shorter sentece.";

var thisLength = getPhraseLength(p1, p2);

console.log(thisLength);



// var btn = document.getElementById("go-button");
//
// function buttonClicked(){
// 	console.log("Button clicked");
//
// 	var customText = document.getElementsByClassName("my-input");
// 	var textArea = document.getElementsByClassName("my-textarea");
// 	var results = document.getElementById("text");
// 	// console.log(customText);
// 	results.innerHTML = "Hello," + customText[0].value + "<br />";
// 	console.log(textArea)
// 	results.innerHTML += "Message: " + textArea[0].value;
// 	console.log(textArea)
// }

// btn.addEventListener("click", buttonClicked);



// var btn = document.getElementById("go-button");
//
// function buttonClicked(){
// 	console.log("Button clicked");
// 	btn.removeEventListener("click", buttonClicked);
// 	document.getElementById("text").innerHTML = "Don't do it!";
// }



// var hobbies = ["pizza", "gaming", "reading", "programming", " music"];
//
// hobbies.push("archery");
// console.log(hobbies.shift);
// hobbies.unshift("blacksmithing");
//
// if(hobbies.indexOf("reading") > -1){
// 	console.log("I'm reading!");
// }
//
// if(hobbies.indexOf("sports") === -1){
// 	console.log("not in array!");
// }
//

//
// var btn = document.getElementById("go-button");
//
//
// function buttonClicked(){
// 	console.log("Button Click");
// 	btn.removeEventListener("click", buttonClicked);
// 	document.getElementById("text").innerHTML = "Don't do it!";
// 	console.log(document.getElementById("text").innerHTML);
// }

// btn.addEventListener("click", buttonClicked);

// function printName(name, age){
// 	console.log("Hello,", name, ". You are", age);
// }
//
// printName("Nick", 22);
// printName("Charles", 56);

// for(var i = 0; i < 10; i++){
// 	console.log("Current i value is", i);
// }

// var isPremiumUser = false;
//
// if(isPremiumUser){
// 	console.log("Thanks for being a loyal customer!")
// }else{
// 	console.log("You should subscribe to our premium service.")
// }
//
// var myAge = 28;
//
// if(myAge < 1){
// 	console.log("You are a baby")
// }else if(myAge < 3){
// 	console.log("You are a toddler")
// }else if(myAge < 10){
// 	console.log("You are a big kid")
// }else if(myAge <= 19){
// 	console.log("You are a teenager")
// }else if(myAge < 40){
// 	console.log("You're an adult.")
// }else{
// 	console.log("You must be old/ you're not in our record!")
// }


// var welcome_message = "This is a welcome message stored inside a variable";
// var myAge = 25;
// var exactAge = 25.555
// alert(welcome_message + exactAge);
// // alert("This is an altert");
// console.log("This is a log");
// console.log("My age next year will be " + myAge);
