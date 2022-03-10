module.exports = function(logger) {
  //default logger
  return logger();
};


module.exports.__module = {
  args: ['utils/logger']
};