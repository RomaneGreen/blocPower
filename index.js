const canCompleteCircuit = function(gas, cost) {

    // length of gas array
      let len = gas.length,
          diff = [],
          curSum = 0,
          sum = 0,
          i,
          startNode = 0;
  
      // loop around  gas,cost and sum values
      for(i = 0; i < len; i++) {
        // sum for diff between gas and cost 
          diff[i] = gas[i] - cost[i];
          sum += diff[i];
          curSum += diff[i];
          
          if (curSum < 0) {
              startNode = i + 1;
              curSum = 0;
          }
      }
      
      // if cant return to start 
      if (sum < 0) {
          return -1;
      } else {
          return startNode;
      }
          
  };


console.log(canCompleteCircuit([2,3,4],[3,4,3]))