const fun = (m,n) =>{
let arr = [];
let sum = 0;
let k = 0;
    for (let i = 0; i < m; i++) {
        arr.push(i);
    }
    console.log(arr);
    for (let i = 1; i < m; i++) {
        sum = arr[i] / 100 + arr[i] / 10 % 10 + arr[i] % 10;
        sum1 = parseInt(sum);
        if (sum1 === n) {
          k++;
            console.log(k, arr[i]);
        }
    }
}
console.log(fun(100, 4))
