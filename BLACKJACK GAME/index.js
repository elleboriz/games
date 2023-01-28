


let sum = 0 ;
let hasBlackJack = false;
let isAlive = false;
let message;
let startGame = document.getElementById('btn');
let newCard  = document.getElementById('btn2');
let msgTag  = document.getElementById('message-el');
let sumParagraph  = document.getElementById('sum');
let cardsParagraph  = document.getElementById('cards');
let cards = []

let player = {
    name :window.prompt('Enter your Name'),
    tips: 200
}


let playerScore = document.getElementById('player-el');
playerScore.textContent = player.name + ": Win Price $"+ player.tips

// let scoreP = document.createElement('p');
// let attrP = document.createAttribute('my-score');



function startGameFunc(){
    
    isAlive = true;
    firstCard = randomCard();
    SecondCard = randomCard();
    cards = [firstCard , SecondCard]
    sum = firstCard + SecondCard
    gameFunc();
}

function randomCard(){
   let value= Math.floor(Math.random()*13)+1
   console.log(value)
   if (value === 1){
    return 11
   }else if (value > 10){
    return 10
   }else{
    return value
   }
}

function gameFunc(){
    


    
/*
Rendering cards in text paragraph and updating each time 
a new card is picked
*/
    cardsParagraph.textContent = "cards: " ;
    for (let i = 0; i < cards.length; i++){
        cardsParagraph.textContent += cards[i]+ " "
    }


    /*
    checking conditions for gameplay rules
    */

    sumParagraph.textContent ="Sum: "+ sum;
    if(sum < 21){
        message= "Do you want to pick a new card?";
        msgTag.textContent = message ;
        
    }
    else if (sum === 21){
        message =  "You'v Got a Black Jack,WIN";
        msgTag.textContent = message ;
        hasBlackJack = true;
        
        
    }
    
    else{
        message= "You are out of the Game!LOST";
        msgTag.textContent = message ;
        isAlive = false ;
    }
    
    console.log(message);
}

function newCardFunc(){
/*
picking new card and automatically adding newcard 
to card list (cards)
*/
    if (isAlive === true && hasBlackJack === false){

    

    console.log('Drawing a new card from the deck');
    let newCard = randomCard();
    sum += newCard

    cards.push(newCard)
    gameFunc()

    }
} 


startGame.onclick = startGameFunc ;
newCard.onclick = newCardFunc;
 


