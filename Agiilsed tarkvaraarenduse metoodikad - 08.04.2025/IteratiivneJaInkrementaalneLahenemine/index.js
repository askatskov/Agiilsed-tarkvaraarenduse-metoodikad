class Patient {
    constructor(nimi, vanus) {
        this.Nimi = nimi;
        this.vanus = vanus;
    }
}

class Arst {
    constructor(nimi, vanus, aeg) {
        this.nimi = nimi;
        this.vanus = vanus;
        this.aeg = aeg;
    }
}

class Haigla {
    constructor() {
        this.patientideList = [];
        this.arstideList = [];
    }

    showAllPatientid() {
        for (let i = 0; i < this.patientideList.length; i++) {
            console.log(this.patientideList[i]);
        }
    }

    showAllarstid() {
        for (let t = 0; t < this.arstideList.length; t++) {
            console.log(this.arstideList[t]);
        }
    }

        showArstiAeg() {
        const arstiNimi = prompt("Milline arst teid huvitab? ");
        const leitudArst = this.arstideList.find(arst => arst.nimi === arstiNimi);
        
        if (leitudArst) {
            console.log("Leitud arst:", leitudArst.aeg);
            this.valiAeg(leitudArst);
        } else {
            console.log("Sellise nimega arsti ei leitud");
            const jätka = prompt("Kas soovite teha jätkata? (jah/ei)").toLowerCase();
            if (jätka === 'jah') {
                this.showArstiAeg();
            }
        }
    }

    valiAeg(arst) {
        const valitudAeg = prompt(`Valige aeg (saadaolevad ajad: ${arst.aeg.join(", ")}): `);
        
        const aegIndex = arst.aeg.indexOf(valitudAeg);
        if (aegIndex !== -1) {
            arst.aeg.splice(aegIndex, 1);
            console.log(`Valisite aja ${valitudAeg}. See aeg on nüüd broneeritud.`);
            
            const jätka = prompt("Kas soovite teha veel broneeringuid? (jah/ei)").toLowerCase();
            if (jätka === 'jah') {
                this.showArstiAeg();
            }
        } else {
            console.log("Vale aeg! Palun valige üks loetletud aegu.");
            this.valiAeg(arst);
        }
    }
}

patsient1 = new Patient("Thomas", 12);
patsient2 = new Patient("Toomas", 15);
patsient3 = new Patient("Koomas", 17);
patsient4 = new Patient("Koobas", 12);

haigla1 = new Haigla();

arst1 = new Arst("Mari", 55, ["10:00", "13:00"]);
arst2 = new Arst("Nari", 45, ["14:00", "17:00"]);

haigla1.arstideList.push(arst1, arst2);
haigla1.patientideList.push(patsient1, patsient2, patsient3, patsient4);

haigla1.showAllPatientid();
haigla1.showAllarstid();
haigla1.showArstiAeg();