/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */

var removeKdigits = function (num, k) {
    const stack = [];
    let remainingToRemove = k;

    for (let digit of num) {
        while (remainingToRemove > 0 && stack.length > 0 && digit < stack[stack.length - 1]) {
            stack.pop();
            remainingToRemove--;
        }
        stack.push(digit);
    }

    while (remainingToRemove > 0) {
        stack.pop();
        remainingToRemove--;
    }

    let result = stack.join('').replace(/^0+/, '');

    if (result === '') return '0';
    return result;
};