var path = require('path'),
  fs = require('fs'),
  jm = require("./utils/json-minify"),
  objectPath = require('object-path'),
  extend = require('extend'),
  _ = require('lodash');


var self = module.exports = {
  data: {},

  templateProcess: function(tpl) {
    if(_.isString(tpl)) {
      return tpl.replace(/^={([\w\.\|]+)}$/, replacer(true)).replace(/\${([\w\.\|]+)}/g, replacer(false));

      function replacer(nothrow) {
        return function(match, varname) {
          var vars = varname.split("|");
          for(var i = 0; i < vars.length; i++) {
            var val = self.get(vars[i]);
            if(val) {
              return val;
            }
          }
          
          if(nothrow) {
            return "";
          }
          
          throw new Error("Cannot replace config variable '" + varname +"' in '"+ tpl +"' because it is undefined");
        }
      }
    } else if(_.isArray(tpl)) {
      var arr = [];
      _.each(tpl, function(val) {
        arr.push(self.templateProcess(val));
      });
      return arr;
    } else if(_.isObject(tpl)){
      var obj = {};
      _.each(tpl, function(val, key) {
        obj[key] = self.templateProcess(val);
      });
      return obj;
    }
    return tpl;
  },

  get: function(key) {
    return self.templateProcess(self.getRaw(key));
  },

  getRaw: function(key) {
    return objectPath.get(self.data, key);
  },

  set: function(key, val) {
    return objectPath.set(self.data, key, val);
  },

  persistDefault: function(key, val, callback) {
    if(!self.get(key)) {
      self.set(key, val);
    }
    self._persist(key, val, 'defaults.gen.json', callback);
  },

  persistOverride: function(key, val, callback) {
    self.set(key, val);
    self._persist(key, val, 'overrides.gen.json', callback);
  },

  _persist: function(key, val, file, callback) {

    file = path.join(self.get('genConfigDir'), file);
    //persist into overrides
    //TODO save/flush on app close?

    //force creation
    fs.closeSync(fs.openSync(file, 'a'));

    fs.readFile(file, 'utf-8', function(err, data) {
      if(err) {
        return callback(err);
      }

      var obj = {};
      if(data) {
        obj = JSON.parse(data);
      }

      objectPath.set(obj, key, val);
      fs.writeFile(file, JSON.stringify(obj, null, "  "), callback);
    });
  },

  mergeChain: function(chain) {
    var args = [true, {}].concat(chain);
    args.push(self.data);

    self.data = extend.apply(null, args);
  },

  /**
   *
   * @param initial
   * @returns config
   */
  initialize: function(init) {
    if(self.initialized) {
      return self;
    }
    self.initialized = true;
    init = init || {};

    var chain = [];

    //TODO push command line too
    
    chain.push(process.env);
    chain.push(init);

    //save chain now to get some initial variables
    self.mergeChain(chain);
    chain = [];
    
    var isDev = self.get('NODE_ENV') ? self.get('NODE_ENV') === 'development' : true;
    var isProd = self.get('NODE_ENV') ? self.get('NODE_ENV') === 'production' : false;
    var env = isDev ? "dev" : 'prod';

    chain.push({
      isDev: isDev,
      isProd: isProd,
      env: env
    });

    //save chain now to get some initial variables
    self.mergeChain(chain);
    chain = [];
    
    //sanitize some important config variables
    var cwd =  path.resolve(self.get('cwd') || process.cwd());
    process.chdir(cwd);

    var appRoot = self.get('appRoot') || cwd;
    var configDir = self.getRaw('configDir') || "${appRoot}/config";
    var genConfigDir = self.getRaw('genConfigDir') || configDir;
    
    chain.push({
      appRoot: appRoot,
      configDir: configDir,
      genConfigDir: genConfigDir,
      cwd: cwd
    });
    self.mergeChain(chain);
    chain = [];

    configDir = self.get('configDir');
    genConfigDir = self.get('genConfigDir');
    
    var genDefaults = path.join(genConfigDir, 'defaults.gen.json');
    if(fs.existsSync(genDefaults)) {
      chain.push(self.getFileData(genDefaults));
    }

    var next = path.join(configDir, 'defaults.json');
    while(next && fs.existsSync(next)) {
      var nextConfig = self.getFileData(next);
      chain.push(nextConfig);

      //get next
      var nextName = nextConfig.next;
      if(nextName) {
        if(typeof nextName !== 'string') {
          nextName = nextName[env];
        }

        next = path.join(configDir, nextName);
      } else {
        next = null;
      }
    }

    var overrides = path.join(genConfigDir, 'overrides.gen.json');
    if(fs.existsSync(overrides)) {
      chain.push(self.getFileData(overrides));
    }

    self.mergeChain(chain);

    return self;
  },
  
  getFileData: function(filename) {
    try {
      return JSON.parse(jm.minify(fs.readFileSync(filename, 'utf-8')));
    } catch(err) {
      throw new Error("Failed to parse config file " + filename + ". Caused by: \n" + err.stack);
    }
  },

  clear: function() {
    self.data = {};
    self.initialized = false;
  }
};