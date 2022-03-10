
var self = module.exports = {
  config: require('./lib/config'),
  logger: require('./lib/utils/logger'),
  promises: require('./lib/utils/promises'),
  
  initialize: function(options) {
    self.config.initialize(options);
  }
};