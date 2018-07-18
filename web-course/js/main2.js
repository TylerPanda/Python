class Animal {
    constructor(name, height, weight) {
        console.log('Created animal named', name)
        this.name = name
        this.height = height
        this.weight = weight
    }
    nameLength() {
        return this.name.length
    }
}

class Dog extends Animal {

    constructor(name, height, weight, barVolume, leashColor) {
        super(name, height, weight);

        this.barVolume = barVolume;
        this.leashColor = leashColor;
    }
    bark() {
        if (this.barVolume > 50) {
            console.log(this.name, "barks loudly! (volume: ", this.barVolume, ")");
        } else {
            console.log(this.name, "barks timidly,(volume: ", this.barVolume, ")");
        }
    }
}


var king = new Dog("King", 45, 92, 72, "red");

king.bark();

// Animal.planet = "Earth";
//
// var dog = new Animal("Fido", 25, 90);
// var fish = new Animal("Goldie", 2, .02);
//
// console.log(dog.constructor.planet);
// console.log(fish.nameLength());

//
// function missingno(numbers){
// 	var missing = -1;
// 	var sorted = numbers.sort(function(a, b){ return a-b; });
//
// 	for(var i = sorted[0]; i <= numbers.length - 1; i++){
// 		if(numbers.indexOf(i) === -1){
// 			missing = i;
// 		}
// 	}
//
// 	return missing;
// }
// var numbers = [3, 8, 7, 9, 6, 4, 12, 5, 14, 19, 16, 18, 11, 10, 13, 17, 20];
// console.log(missingno(numbers));
