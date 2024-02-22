#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const completedDict = {}


request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
    for (const element of data) {
      if (!(element.userId in completedDict)) {
        if (element.completed === true) {
	  completedDict[element.userId] = 1;
			
	}
		
      } else {
	if (element.completed === true) {
		completedDict[element.userId] = completedDict[element.userId] + 1;
	}
      }
    }
    console.log(completedDict);
});
