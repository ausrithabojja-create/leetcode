/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
Array.prototype.last = function() {
    return this.length ? this[this.length - 1] : -1;
};
