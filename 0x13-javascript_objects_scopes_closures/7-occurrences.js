#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const occurrences = list.reduce((count, element) => {
    return count + (element === searchElement ? 1 : 0);
  }, 0);

  return occurrences;
};
