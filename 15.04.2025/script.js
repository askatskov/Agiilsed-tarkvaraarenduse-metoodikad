// Nimekirjad ja klassid
const nameList = [
    'Time','Past','Future','Dev','Fly','Flying','Soar','Soaring','Power','Falling',
    'Fall','Jump','Cliff','Mountain','Rend','Red','Blue','Green','Yellow','Gold',
    'Demon','Demonic','Panda','Cat','Kitty','Kitten','Zero','Memory','Trooper','XX',
    'Bandit','Fear','Light','Glow','Tread','Deep','Deeper','Deepest','Mine','Your',
    'Worst','Enemy','Hostile','Force','Video'
];

const itemList = ['Power', 'Trooper', 'Basic', 'Toy', 'Weapon', 'Tool'];

class Platform {
    constructor(resources) {
        this.resources = resources;
    }
}

class People {
    constructor(name, age, gender, item) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.item = item;
    }

    consume(platform) {
        let baseAmount = 5;

        if (this.age > 60) {
            baseAmount += 5;
        }

        if (this.gender === 'male') {
            baseAmount += 2;
        } else if (this.gender === 'female') {
            baseAmount -= 1;
        }

        if (this.item === 'Power' || this.item === 'Trooper') {
            baseAmount += 3;
        }

        baseAmount = Math.max(0, baseAmount);
        platform.resources = Math.max(0, platform.resources - baseAmount);

        console.log(`${this.name} (${this.gender}, ${this.age}a) kasutas ${baseAmount} ressurssi. Alles: ${platform.resources}`);
    }
}

let platform1 = new Platform(100);

let peopleList = [];

for (let i = 0; i < 5; i++) {
    let person = new People(
        nameList[Math.floor(Math.random() * nameList.length)],
        Math.floor(Math.random() * 100),
        Math.random() > 0.5 ? 'male' : 'female',
        itemList[Math.floor(Math.random() * itemList.length)]
    );

    peopleList.push(person);
}

peopleList.forEach(person => {
    person.consume(platform1);
});
