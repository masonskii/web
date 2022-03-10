var winston = require('winston'),
  config = require("../config"),
  _ = require('lodash');

//Logger is not 'scattered' because should be available before container
//initialization

var LEVELS = [
  'silly',
  'verbose',
  'info',
  'warn',
  'debug',
  'error'
];


var DEFAULT_CONFIG = {
  "config": {
    "console": {
      prettyPrint: true,
      level: "info",
      colorize: true
    }
  }
};

function createLogMethod(logger, level) {
  logger[level] = function(/*message, meta*/) {
    var args = Array.prototype.slice.apply(arguments);
    args.splice(0, 0, level);
    logger.log.apply(logger, args);
  };
}

/**
 *
 * @param name
 * @param winstonLogger
 * @constructor
 */
function Logger(name, winstonLogger) {
  this.name = name;
  this.winston = winstonLogger;

  for( var i = 0; i < LEVELS.length; i++) {
    createLogMethod(this, LEVELS[i]);
  }
}

Logger.prototype.log = function(/*level, message, meta or params*/) {
  var args = Array.prototype.slice.call(arguments);
  args[1] = "["+this.name+"] " + args[1];
  if(this.winston) {
    this.winston.log.apply(this.winston, args);
  }
};

Logger.prototype.startProfiling = function(name, autoStart, level) {
  var profiler = new Profiler(this, name, level);
  if(autoStart) {
    profiler.start();
  }
  return profiler;
};

Logger.prototype.getProfiler = function(name, level) {
  return new Profiler(this, name, level);
};

/**
 *
 * @param logger
 * @param name
 * @param level
 * @constructor
 */
function Profiler(logger, name, level) {
  this.logger = logger;
  this.name = name;
  this.times = 0;
  this.diff = 0;
  this.paused = true;
  this.level = level || 'verbose';
}

Profiler.prototype.start = function() {
  this.time = Date.now();
  this.times++;
  this.paused = false;
  this.logger.log(this.level, "Starting profiling ["+this.name+"]");
};

Profiler.prototype.pause = function() {
  if(!this.paused) {
    this.diff += Date.now() - this.time;
    this.paused = true;
  }
};

Profiler.prototype.end = function() {
  if(!this.paused) {
    this.diff += Date.now() - this.time;
  }
  this.logger.log(this.level, "Profiler ["+this.name+"] executed "+this.times+" time(s) in " +
    this.diff + "ms");
};


var cache = {};

/**
 *
 * @type {Function}
 */
var logger = module.exports = function(name) {
  var defaultLoggerConfig = config.get('logger.default') || DEFAULT_CONFIG;
  name = name || "Default";
  if(typeof cache[name] === 'undefined') {
    var moduleConf = config.get('logger.modules.'+name);
    //noinspection JSCheckFunctionSignatures
    moduleConf = _.extend({}, defaultLoggerConfig, moduleConf);

    if(!moduleConf.disabled) {
      //initialize
      winston.loggers.add(name, moduleConf.config);
      var winstonLogger = winston.loggers.get(name);
      cache[name] = new Logger(name, winstonLogger);
    } else {
      cache[name] = new Logger(name, null);
    }
  }
  return cache[name];
};

module.exports.__module = {
  type: 'object'
};
