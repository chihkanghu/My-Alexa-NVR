"use strict"
var APP_ID = undefined;
var AlexaSkill = require('./AlexaSkill');
let MyCommand = require("./sendCommand");
let sendCommand = new MyCommand("steve.io/myNVR")

var MyNVR = function () {
    AlexaSkill.call(this, APP_ID);
};

MyNVR.prototype = Object.create(AlexaSkill.prototype);
MyNVR.prototype.constructor = MyNVR;

MyNVR.prototype.eventHandlers.onSessionStarted = function (sessionStartedRequest, session) {
    console.log("MyNVR onSessionStarted requestId: " + sessionStartedRequest.requestId
        + ", sessionId: " + session.sessionId);
};

MyNVR.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    console.log("MyNVR onLaunch requestId: " + launchRequest.requestId + ", sessionId: " + session.sessionId);
};

MyNVR.prototype.eventHandlers.onSessionEnded = function (sessionEndedRequest, session) {
    console.log("MyNVR onSessionEnded requestId: " + sessionEndedRequest.requestId
        + ", sessionId: " + session.sessionId);
};

MyNVR.prototype.intentHandlers = {
   "PlaybackIntent": function (intent, session, response) {
        var speechOutput = "Play NVR recordings.";
        var req = {"playback": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
   "StopPlayingIntent": function (intent, session, response) {
        var speechOutput = "Stop playing.";
        var req = {"playstop": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
   "GoSixteenIntent": function (intent, session, response) {
        var speechOutput = "Sixteen view.";
        var req = {"sixteen": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
   "GoQuadIntent": function (intent, session, response) {
        var speechOutput = "Quad view.";
        var req = {"quad": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
   "FastForwardIntent": function (intent, session, response) {
        var speechOutput = "Fast forward.";
        var req = {"fastforward": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
   "FastRewindIntent": function (intent, session, response) {
        var speechOutput = "Fast rewind.";
        var req = {"fastrewind": "nvr"};
        sendCommand.sendCommand(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
        });
   },
  "ChangeChannelIntent": function (intent, session, response) {
       if(!intent.slots.Channel || !intent.slots.Channel.value) {
            response.ask("Say channel number from one to sixteen.", "Say channel number from one to sixteen.");
            return;
       }

       let channelRequested = intent.slots.Channel.value;
       var speechOutput = "Swtich to " + "channel " + channelRequested + ".";

       var req = {"channel": Number(channelRequested)};
        
       sendCommand.sendChannel(req, () => {
            response.tellWithCard(speechOutput, "My NVR", speechOutput);
      });
   },

   "AMAZON.HelpIntent": function (intent, session, response) {
        response.tell("You can ask me to operate your NVR, play, stop, or go live. You can also ask me to switch channel and return 16-way.")
    }
};

exports.handler = function (event, context) {
    var instance = new MyNVR();
    instance.execute(event, context);
};
