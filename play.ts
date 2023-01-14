import chat from "prompt-sync";
let prompt = chat();

const guess = (x: string[]) => {
  let serverd: string[] = [];
  let predit_serverd: string[] = [];

  console.log(arr_of_basket);

  for (let i = 1; i <= 3; i++) {
    let value: number = Math.floor(Math.random() * x.length);
    serverd.push(x[value]);
  }

  for (let i = 1; i <= 3; i++) {
    let value: string = prompt(`The ${i} Prediction is: `);
    predit_serverd.push(value);
  }

  //   console.log(serverd, predit_serverd);
  
  let emp: boolean[] = [];

  serverd.forEach((e) => {
    predit_serverd.some((el) => {
      emp.push(e === el);
    });
  });

  console.log(emp);
};

let arr_of_basket: string[] = [
  "orange",
  "apple",
  "olive",
  "pine-apple",
  "banana",
  "lemon",
  "peach",
  "pear",
  "watermelon",
  "coconut",
];

guess(arr_of_basket);
