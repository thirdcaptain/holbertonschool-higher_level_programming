#!/usr/bin/node
// Base 10 converter
exports.converter = function (base) {
  return function (y) {
    return y.toString(base);
  };
};
