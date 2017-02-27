"use strict"

var mqtt = require('./node_modules/mqtt');

class Send {
  constructor(topic) {
    this.topic = topic;
  }

  sendChannel(req, done) {
    var ops = { port: 1883, host: "mqtt.cc" };

    var client = mqtt.connect(ops);

    client.on('connect', () => {
      console.log("MQTT Connected");
      let payload = req;
      let cb = () => {
        done();
      };
      client.publish(this.topic, JSON.stringify(payload), {qos: 1}, cb);
    });
  }
  sendCommand(req, done) {
    var ops = { port: 1883, host: "mqtt.cc" };

    var client = mqtt.connect(ops);
    let cb = () => {
      done();
    };
    client.on('connect', () => {
      console.log("Connected");
      let payload = req;
      client.publish(this.topic, JSON.stringify(payload), {qos: 1}, cb);
    });
  }
}

module.exports = Send;