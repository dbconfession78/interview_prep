// given a mathematical expression as a string
// write a function that evaluates the expression
// should respect the order of operations
// will only contain intergers, p (+), m (-), d (/), x (x)



function evalStr(str) {
  let stk = [];
  let ops = [];
  let i = 0;
  let sNum = "";
  let num;
  while (i < str.length) {
    sNum += str[i];
    // if the next char is a letter
    // prepare the string
    if (i < str.length && isNaN(str[i+1])) {
      num = parseInt(sNum);
      sNum = "";
      const op = str[i+1];
      if (stk.length === 0) {
        stk.push(num);
        ops.push(op);
        i +=1;
      } else {
        if (ops[ops.length-1] === "x" || ops[ops.length-1] === "d") {
          const o = ops.pop();
          const num2 = stk.pop();
          let res;
          if (o == "x") {
            res = num * num2;
          } else {
           res = num2 / num;
          }

          stk.push(res);
          if (op != undefined) {
              ops.push(op);

          }
          i += 1
        } else {

          stk.push(num);
          if (op != undefined) {
              ops.push(op);
          }

          i += 1
        }
      }
    }
    i += 1;
  }
  i = 0;
  let x = 1;
  let retval = stk[0]
  while(i < ops.length) {
    const op = ops[i];
    const a = stk[x];
    x += 1
    if (op === "m") {
        retval -= a;
    } else {
        retval += a;
    }

    i += 1;
  }
  return retval;
}

console.log(evalStr("11p2d2")); // 12
console.log(evalStr("12d6m2")); // 0
console.log(evalStr("12x2p4p4p4m2d2")); // 35
