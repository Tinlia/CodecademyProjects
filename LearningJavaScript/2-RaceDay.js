/*
Evan Kimpton / Tinlia

Context: The annual race is around the corner. This year, there are a lot of participants. The race timeline is as follows: 
09:30 am - Adults and registered early
11:00 am - Adults and registered late
12:30 pm - All youth
Adults are anyone above the age of 18, youth are anyone below.

Objective: Write a program to register runners for the race and give them instructions on race day.

*/

let raceNumber = Math.floor(Math.random() * 1000);
var registerEarly = true; // Can also be set to false
var runnerAge = 2; // Can be changed
if(runnerAge > 18 && registerEarly){
  raceNumber += 1000;
  console.log(`Thank you for registering. Your runner number is ${raceNumber}, and you will be running at 9:30 am.`);
} // If the runner is an early adult, they race at 9:30 am
else if(runnerAge > 18 && registerEarly === false){
  raceNumber += 1000;
  console.log(`Thank you for registering. Your runner number is ${raceNumber}, and you will be running at 11:00 am.`);
} // If the runner is a late adult, they race at 11:00 am
else if(runnerAge < 18){
  console.log(`Thank you for registering. Your runner number is ${raceNumber}, and you will be running at 12:30 pm.`);
} // If the runner is a youth, they race at 12:30 pm
else{
  console.log('Please see the registration desk.');
} // If the runner is 18, they are sent to the registration desk
