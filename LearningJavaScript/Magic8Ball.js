/*
Evan Kimpton / Tinlia

Objective: Create a magic 8 ball using ternary expressions and switch statements in JavaScript
*/

var userName = 'Tinlia'; // Name instert is optional
userName
? console.log(`[Eight Ball]: Hello, ${userName}!`)
: console.log('[Eight Ball]: Hello!');

var userQuestion = 'Will a question be put here?'; // Insert a question here
userQuestion
? userName
  ? console.log(`[${userName}]: ${userQuestion}?`)
  : console.log(`[Stranger]: ${userQuestion}?`)
: console.log('No question expressed, rolling for fun.');

var randomNumber = Math.floor(Math.random() * 8);
var eightBall = '';

switch(randomNumber){
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
    eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
    eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break;
  case Neutral:
    break;
} // Chooses a random response from 8 choices

console.log(`[Eight Ball]: ${eightBall}.`);
